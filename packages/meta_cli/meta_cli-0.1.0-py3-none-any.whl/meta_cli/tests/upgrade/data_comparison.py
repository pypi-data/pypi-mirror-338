import base64

import pytest
from loguru import logger
from deepdiff import diff

from meta_cli.core.command_builder import ChainClient
from meta_cli.tests.me_hub.kyc import TestKyc


@pytest.mark.usefixtures("me_client_v1", "me_client_v2")
class TestUpgradeDataComparison:
    fork_height = 4237670
    upgrade_height = 4251100

    @classmethod
    @pytest.fixture(autouse=True)
    def inject_tester(cls, me_client_v1: ChainClient, me_client_v2: ChainClient, ):
        cls.me_client_v1 = me_client_v1
        cls.me_client_v2 = me_client_v2
        cls.kyc_instance = TestKyc.create_instance(None, me_client_v2, None)

    def test_kyc_info_by_region(self):
        """
        测试升级前后kyc总量
        1. 目前1.3中validator_meids:282600000000 有这么多kyc用户，但目前接口查所有kyc单次最多返回1000条数据，并且不支持查下一页
        2. 2.0中一个区域下的kyc数据为'total': '1066'，与查询validator_meids: 106600000000 数据一致
        3. 但是步骤1，2 中的kyc总数就不一致
        """
        region_id = "chn"

        def kyc_total_count(client, region_id):
            if client.cli_path == "med":
                resp = client.execute(client.build("q", "kyc", ["KYCs"], **{"region": region_id, "count-total": "",
                                                                            "height": self.upgrade_height}))
                me_ids = resp["KYCs"]
                count_total = resp["pagination"]
                logger.info(f"me_ids: {len(me_ids)}, KYC total count: {count_total}")
            else:
                resp = client.execute(client.build("q", "staking", ["meid-by-region", region_id],
                                                   **{"height": self.fork_height}))
                me_ids = resp["meid"]
                total_count = len(me_ids)
                # not support page-key
                # if resp["pagination"]["next_key"] is not None and not "":
                #     while True:
                #         resp = client.execute(client.build("q", "staking", ["meid-by-region", region_id],
                #                                            **{"page-key": resp["pagination"]["next_key"]}))
                #         total_count += len(resp["meid"])
                #         if resp["pagination"]["next_key"] is None or "":
                #             break
                logger.info(f"total_count:{total_count}")

            if client.cli_path == "med":
                resp1 = client.execute(
                    client.build("q", "staking", ["region", region_id], **{"height": self.upgrade_height}))
            else:
                resp1 = client.execute(
                    client.build("q", "staking", ["show-region", region_id], **{"height": self.fork_height}))

            operator_address = resp1.get("region", None)["operator_address"]
            logger.info(operator_address)

            if client.cli_path == "med":
                resp2 = client.execute(client.build("q", "staking", ["validator", operator_address],
                                                    **{"height": self.upgrade_height}))
            else:
                resp2 = client.execute(client.build("q", "staking", ["validator", operator_address],
                                                    **{"height": self.fork_height}))
            logger.info(f"validator_meids:{resp2['meid_amount']}")

        kyc_total_count(self.me_client_v1, region_id)
        logger.info("client_v2")
        kyc_total_count(self.me_client_v2, region_id)

    def test_node_staking(self):
        v1_validators = self.me_client_v1.execute(self.me_client_v1.build("q", "staking", ["validators", ]))
        print(v1_validators)
        v2_validators = self.me_client_v2.execute(self.me_client_v2.build("q", "staking", ["validators", ]))

        v1_info = v1_validators['validators']
        v2_info = v2_validators['validators']
        for v1 in v1_info:
            operator_address = v1['operator_address']
            for v2 in v2_info:
                if operator_address == v2["operator_address"]:
                    resp = diff.DeepDiff(v1, v2)
                    print(f"operator_address:{operator_address},")
                    print(f"resp.values: {resp.tree["values_changed"]}")
                    # print(f"resp.values: {resp.tree['dictionary_item_added']}")
                    # assert v1['staker_shares'] == v2['delegator_shares']
                    pass

    def test_region_info(self):
        v1_region = self.me_client_v1.execute(self.me_client_v1.build("q", "staking", ["list-region"],
                                                                      **{"height": self.fork_height}))
        v2_region = self.me_client_v2.execute(self.me_client_v2.build("q", "staking", ["regions", ],
                                                                      **{"height": self.upgrade_height}))
        v1_info = v1_region['region']
        v2_info = v2_region['region']
        for v1 in v1_info:
            region_id = v1['regionId']
            for v2 in v2_info:
                if region_id == v2["regionId"]:
                    resp = diff.DeepDiff(v1, v2)
                    print(f"region_id:{region_id},")
                    print(f"resp.values: {resp.tree["values_changed"]}")
                    # print(f"resp.values: {resp.tree['dictionary_item_added']}")
                    # assert v1['staker_shares'] == v2['delegator_shares']

        # 监控不同区块下nga的区域信息
        # for height in range(self.fork_height, self.upgrade_height):
        #     resp1 = self.me_client_v1.execute(self.me_client_v1.build("q", "staking", ["show-region", "nga"],
        #                                                               **{"height": height}))
        #     logger.info(resp1['region']["delegate_amount"])
        #     if resp1['region']["delegate_amount"] == "0":
        #         break
        #     print(resp1)

        # resp2 = self.find_first_zero_delegate()
        # print(resp2)

    def find_first_zero_delegate(self):
        low = self.fork_height
        high = self.upgrade_height
        first_zero_height = None  # 记录第一个出现0的高度

        while low <= high:
            mid = (low + high) // 2
            resp = self.me_client_v2.execute(
                self.me_client_v2.build("q", "staking", ["region", "nga"], **{"height": mid})
            )
            current_amount = resp['region']["delegate_amount"]

            if current_amount == "0":
                # 找到0，尝试向左找更早的0
                first_zero_height = mid
                high = mid - 1
            else:
                # 当前高度非0，向右查找
                low = mid + 1

        return first_zero_height

    @pytest.mark.P2
    def test_group_v1_v2_reward(self):
        """
        1. 创建一个kyc用户并加入社区
        2. 造一个uat已加过群，但是退群的账号信息，验证在u2.0升级后再次加群，不会发送奖励信息,优先级低，影响范围小
        """
        address, _ = self.kyc_instance.test_kyc()
        global_dao = self.me_client_v2.query_create_address("global_dao")
        self.me_client_v2.transfer_coin(global_dao, address, "100000000", fees="40000")

        cmd = self.me_client_v2.build("tx", "megroup", ["join-group", 1000000049, address],
                                      **{"from": address, "fees": f"4000{self.me_client_v2.denom}"})
        resp = self.me_client_v2.execute(cmd)
        pass

    def test_v2_FixedDepositPrincipalPool(self):
        """
        region/fixed_deposit_amount = FixedDepositPrincipalPool
        """
        fixed_deposit_principal_pool = self.me_client_v2.query_create_address("fixed_deposit_principal_pool",
                                                                              target="remote")
        fixed_deposit_principal_pool_balances = self.me_client_v2.query_balance(fixed_deposit_principal_pool)

        regions = self.me_client_v2.get_regions()

        fixed_deposit_amount = [{i["regionId"]: int(i['fixed_deposit_amount'])} for i in regions['region']]
        print(fixed_deposit_amount)

        print(fixed_deposit_principal_pool_balances)
        print(sum(value for d in fixed_deposit_amount for value in d.values()))

        fixed = self.me_client_v2.execute(self.me_client_v2.build("q", "staking", ["list-fixed-deposit"],
                                                                  **{"limit": 10000}))

        amount = sum(int(i.get('principal')['amount']) for i in fixed['FixedDeposit'])

        logger.info(f"all fixed deposit: {len(fixed['FixedDeposit'])}")
        logger.info(f"all fixed deposit amount: {amount}")
        pass
