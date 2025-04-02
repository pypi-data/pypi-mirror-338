import pytest
from loguru import logger

from meta_cli.core.command_builder import ChainClient
from meta_cli.tests.base import BaseChainTest
from meta_cli.core import common_assert as ca
from meta_cli.tests.me_hub.kyc import TestKyc


@pytest.mark.usefixtures("da_client", "me_client", "rollup_client")
class TestStaking(BaseChainTest):
    """
    Test class for staking-related functionalities.
    Uses pytest fixtures to inject dependencies.
    """

    @pytest.fixture(autouse=True)
    def _init_kyc_instance(self, da_client, me_client, rollup_client):
        """在测试开始时初始化 kyc_instance"""
        self.kyc_instance = TestKyc.create_instance(da_client=da_client,
                                                    me_client=me_client,
                                                    rollup_client=rollup_client)

    def test_withdraw_from_region(self):
        """
        Test case for withdraw from a region.
        It builds and executes a staking withdrawal transaction, then verifies the transaction success.
        """
        # uat global_dao != super, 兼容测试环境用户而已
        global_dao = self.me_client.query_create_address("global_dao")
        amount = 1000 * 10 ** 8

        cmd = self.me_client.build("tx", "staking", ["withdraw-from-region",
                                                     "chn", global_dao,
                                                     f"{amount}{self.me_client.denom}"],
                                   **{"from": "super", "gas": "500000"})
        file_path = "tx.json"
        cmd += f" --generate-only > {file_path}"
        resp = self.me_client.execute(cmd)
        assert resp.get("raw") == ''
        resp = self.me_client.hub_super_sign(file_path)
        ca.assert_tx_success(self.me_client, resp)

    def test_deposit_fixed(self):
        """
        Test case for depositing a fixed amount.
        It verifies the user's KYC status, transfers coins, executes a deposit transaction, and checks the updated region and user balances.
        """
        global_dao = self.me_client.query_create_address("global_dao")
        region_id = "chn"
        region_info = self.me_client.get_regions(region_id=region_id)
        # 1. new-kyc user
        user1_addr, _ = self.kyc_instance.test_kyc(region_id=region_id)
        assert user1_addr is not None and isinstance(user1_addr, str)
        base_amount = 1 * 10 ** 8

        amount = 10 * 10 ** 8
        fees = 4000

        self.me_client.transfer_coin(
            global_dao, user1_addr, base_amount + amount, fees=str(fees))

        cmd = self.me_client.build("tx", "staking",
                                   ["deposit-fixed",
                                    f"{amount}{self.me_client.denom}", "1", ],
                                   **{"from": user1_addr, "fees": f"{fees}{self.me_client.denom}"})
        resp = self.me_client.execute(cmd)
        tx_receipt = ca.assert_tx_success(self.me_client, resp)
        logger.info(tx_receipt)

        region_info_after = self.me_client.get_regions(region_id=region_id)
        user1_balance_after = self.me_client.query_balance(user1_addr)

        ca.assert_values_equal(region_info_after["region"]["delegate_amount"], int(
            region_info["region"]["delegate_amount"]) + base_amount)
        ca.assert_values_equal(
            region_info_after["region"]["fixed_deposit_amount"], int(
                region_info["region"]["fixed_deposit_amount"]) + int(amount))
        pass
