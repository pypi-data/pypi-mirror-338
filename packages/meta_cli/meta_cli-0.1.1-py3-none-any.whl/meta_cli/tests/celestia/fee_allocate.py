import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

import pytest
from loguru import logger

from meta_cli.core.command_builder import ChainClientFactory, ChainClient
from meta_cli.core import common_assert as ca

DESTINATION_EVENT_QUERY = "tm.event='Tx' AND message.action='/ibc.core.channel.v1.MsgRecvPacket'"
SOURCE_EVENT_QUERY = "tm.event='Tx' AND message.action='/ibc.core.channel.v1.MsgAcknowledgement'"
FEE_ALLOCATE_EVENT_QUERY = "tm.event='Tx' AND message.action='/celestia.fee.v1.MsgAllocateFee'"


def test_update_and_query_basic_params(da_client):
    """
    测试修改手续费的基础配置
    - 只有dao地址才有权限更改
    - 可以修改 feeTreasuryAddress, devOperatorAddress, allocatePeriod
    :case
    - 1. 使用非dao地址修改相关地址
    - 2. 使用dao修改相关地址
    - 3. allocatePeriod参数异常场景[0.5, -1, 0, 1, 100]
    - 4. 查询相关配置信息
    :param da_client:
    :return:
    """
    dao = da_client.query_create_address("dao")
    no_dao = da_client.query_create_address("no_dao")

    # params
    feeTreasuryAddress = da_client.query_create_address("feeTreasuryAddress")
    devOperatorAddress = da_client.query_create_address("devOperatorAddress")
    allocatePeriod = "50"

    # - 1. 使用非dao地址修改相关地址
    da_client.transfer_coin(dao, no_dao, "50000")

    tx_resp = da_client.execute(da_client.build("tx", "feeAllocate", ["update-basic-params",
                                                                feeTreasuryAddress, devOperatorAddress,
                                                                allocatePeriod], **{"from": no_dao}))
    logger.info(tx_resp)
    assert tx_resp["code"] == 13 and "insufficient fee" in tx_resp["raw_log"]

    tx_resp = da_client.execute(da_client.build("tx", "feeAllocate",
                                          ["update-basic-params", feeTreasuryAddress, devOperatorAddress,
                                           allocatePeriod], **{"from": no_dao, "fees": "10000udmec"}))
    logger.info(tx_resp)
    assert tx_resp["code"] == 0
    tx_receipt = da_client.wait_for_tx_confirmation(tx_resp["txhash"])
    assert tx_receipt["code"] == 11201 and "permission denied" in tx_receipt["raw_log"]

    # - 2. 使用dao修改相关地址
    cmd = da_client.build("tx", "feeAllocate",
                       ["update-basic-params", feeTreasuryAddress, devOperatorAddress,
                        allocatePeriod], **{"from": dao})
    tx_resp = da_client.execute(cmd)
    assert tx_resp["code"] == 0
    assert da_client.wait_for_tx_confirmation(tx_resp["txhash"])['code'] == 0

    # - 3. allocatePeriod参数异常场景[0.5, -1, 0, 1, 100]
    for period in [-1, 0.5, 0, 1, 10]:
        tx_resp = da_client.execute(da_client.build("tx", "feeAllocate",
                                              ["update-basic-params", feeTreasuryAddress, devOperatorAddress,
                                               f"{period}"], **{"from": dao}))
        logger.info(tx_resp)
        if period == -1:
            assert "unknown shorthand flag: '1' in -1" in tx_resp.get("raw")
        elif period == 0.5:
            assert "strconv.ParseUint error.err" in tx_resp.get("raw")
        elif period == 0 or period == 1:
            assert "Error: AllocationPeriod" in tx_resp.get("raw")
        else:
            assert tx_resp["code"] == 0
            tx_receipt = da_client.wait_for_tx_confirmation(tx_resp["txhash"])
            logger.info(tx_receipt)
            assert tx_receipt["code"] == 0

    # - 4. 查询相关配置信息
    query_resp = da_client.execute(da_client.build(
        "query", "feeAllocate", "basic-params"))
    logger.info(query_resp)
    assert query_resp["allocate_basic_param"].get("allocation_period") == 10
    assert query_resp["allocate_basic_param"].get(
        "fee_treasury_address") == feeTreasuryAddress
    assert query_resp["allocate_basic_param"].get(
        "dev_operator_address") == devOperatorAddress

    pass


def test_update_and_query_fee_allocate_rate(da_client):
    """
    测试修改手续费的分配比例
    - feeTreasuryRate, feeDevOperatorRate 只有dao地址才有权限更改
    验证场景：
    - 非DAO地址无权限修改
    - DAO地址修改时的参数校验
    - 正常修改后的状态查询

    Case 设计：
    - 权限验证：非DAO地址操作应失败
    - 异常参数：负数、超范围值、小数、总和非100
    - 有效参数：边界值(0/100)和有效组合
    :param client:
    :return:
    """
    no_dao = da_client.query_create_address("no_dao")
    dao = da_client.query_create_address("dao")
    da_client.transfer_coin(dao, no_dao, "10000")

    case = {
        "case": "非dao地址操作",
        "params": (50, 50),
        "expected": {
            "error": False,
            "check_fail": False,
            "deliver_fail": True,
            "success": False,
            "patterns": {"code": 11201,
                         "value": "permission denied"}  # 预期包含的错误关键词
        }
    }

    # ---------- 阶段1：非DAO地址操作 ----------
    resp = da_client.execute(
        da_client.build("tx", "feeAllocate",
                     ["update-fee-allocate-rate", *case["params"]], **{"from": no_dao, "fees": f"10000{da_client.denom}"}))
    ca.common_assert(da_client, resp, case)

    # ---------- 阶段2：DAO地址异常参数测试 ----------
    invalid_cases = [
        {
            "case": "负数测试",
            "params": (-1, 101),
            "expected": {
                "error": True,
                "check_fail": False,
                "deliver_fail": False,
                "success": False,
                "patterns": {
                    "value": "unknown shorthand flag"
                }
            }
        },
        {
            "case": "总和超限",
            "params": (100, 100),
            "expected": {
                "error": True,
                "check_fail": False,
                "deliver_fail": False,
                "success": False,
                "patterns": {
                    "value": "must be 100"
                }
            }
        },
        {
            "case": "小数参数",
            "params": (0.5, 99.5),
            "expected": {
                "error": True,
                "check_fail": False,
                "deliver_fail": False,
                "success": False,
                "patterns": {
                    "value": "strconv.ParseUint error.err"
                }
            }
        },
        {
            "case": "不足100",
            "params": (1, 98),
            "expected": {
                "error": True,
                "check_fail": False,
                "deliver_fail": False,
                "success": False,
                "patterns": {
                    "value": "must be 100"
                }
            }
        }
    ]

    for case in invalid_cases:
        treasury, dev = case["params"]
        resp = da_client.execute(
            da_client.build("tx", "feeAllocate",
                         ["update-fee-allocate-rate", treasury, dev], **{"from": dao}))
        ca.common_assert(da_client, resp, case)

    # ---------- 阶段3：有效参数测试 ----------
    valid_cases = [
        {
            "case": "边界值",
            "params": (0, 100),
            "expected": {
                "error": False,
                "check_fail": False,
                "deliver_fail": False,
                "success": True,
                "patterns": {},
                "query_check": {  # 需要验证的查询结果
                    "fee_treasury_rate": 0,
                    "dev_operator_rate": 100
                }
            },
        },
        {
            "case": "有效组合",
            "params": (33, 67),
            "expected": {
                "error": False,
                "check_fail": False,
                "deliver_fail": False,
                "success": True,
                "patterns": {},
                "query_check": {
                    "fee_treasury_rate": 33,
                    "dev_operator_rate": 67
                }
            }
        },
    ]

    for case in valid_cases:
        # 提交修改
        treasury, dev = case["params"]
        resp = da_client.execute(
            da_client.build("tx", "feeAllocate",
                         ["update-fee-allocate-rate", treasury, dev], **{"from": dao}))
        ca.common_assert(da_client, resp, case)

        # 验证状态
        query_resp = da_client.execute(
            da_client.build("q", "feeAllocate", ["allocate-rate"]))
        ca.assert_query_match(query_resp, "allocate-rate",
                              case["expected"]["query_check"])


def test_withdraw_treasury_fee(da_client, me_client):
    """
    测试金库提取手续费
    - 只有dao地址才有权限提取
    - 提取至celestia网络地址
    - 提取至me网络地址,使用ibc跨链
    :param client:
    :return:
    """
    receiver_fee = da_client.query_create_address("receiver_fee")
    dao = da_client.query_create_address("dao")
    no_dao = da_client.query_create_address("no_dao")
    amount = "100"
    da_client.transfer_coin(dao, no_dao, "20000")
    da_client.transfer_coin(no_dao, dao, "10000", fees="4000")

    cases = [
        {
            "case": "非dao地址提取金额手续费",
            "params": ("src-port", "src-channel", receiver_fee, amount, "false"),
            "expected": {
                "error": False,
                "check_fail": False,
                "deliver_fail": True,
                "success": False,
                "patterns": {
                    "code": 11201,
                    "value": "permission denied"
                },
            }
        },
    ]
    for case in cases:
        resp = da_client.execute(
            da_client.build("tx", "feeAllocate",
                         ["withdraw-treasury-fee", *case["params"]], **{"from": no_dao, "fees": "1000" + da_client.denom}))
        ca.common_assert(da_client, resp, case)

    valid_cases = [
        {
            "case": "dao地址提取金额手续费-至celestia网络地址",
            "params": ("src-port", "src-channel", receiver_fee, amount, "false"),
            "expected": {
                "error": False,
                "check_fail": False,
                "deliver_fail": False,
                "success": True,
                "patterns": {},
            }
        },

    ]

    for case in valid_cases:
        before_balance = da_client.query_balance(receiver_fee)

        resp = da_client.execute(
            da_client.build("tx", "feeAllocate",
                         ["withdraw-treasury-fee", *case["params"]], **{"from": dao, "fees": "1000" + da_client.denom}))
        ca.common_assert(da_client, resp, case)

        after_balance = da_client.query_balance(receiver_fee)
        assert int(after_balance["amount"]) == int(before_balance["amount"]) + int(amount)

    ibc_transfer_cases = [
        {
            "case": "dao地址提取金额手续费-至me网络地址",
            "params": ("transfer", da_client.channels.get("to_me"), receiver_fee, amount, "true"),
            "expected": {
                "error": False,
                "check_fail": False,
                "deliver_fail": False,
                "success": True,
                "patterns": {},
            }
        },
    ]
    for case in ibc_transfer_cases:
        before_balance = me_client.query_balance(receiver_fee)

        resp = da_client.execute(
            da_client.build("tx", "feeAllocate",
                         ["withdraw-treasury-fee", *case["params"]], **{"from": dao, "fees": "1000" + da_client.denom}))
        tx_receipt = ca.common_assert(da_client, resp, case)
        print(tx_receipt)
        # TODO
        #  1. 监听某个服务告知transfer交易完成后在去查询余额  - Done
        #  2. 异步处理逻辑中需要加上 time-out-block 和 time-out,这个两个参数通过 tx_receipt 获取
        #  3. 同步逻辑中启动一个线程去监听事件
        resp = da_client.sync_subscribe(SOURCE_EVENT_QUERY)

        after_balance = me_client.query_balance(receiver_fee)
        assert int(after_balance["amount"]) == int(
            before_balance["amount"]) + int(amount)


def test_fees_gather_allocate(da_client):
    """
    测试业务流程，手续费收取与分配
    - 1. 普通用户发起交易 模块账户收取到fees
    - 2. 等待到分配的区块高度
    - 3. 验证到指定区块高度后，手续费金库与项目方地址余额
    :param client:
    :return:
    """
    dao = da_client.query_create_address("dao")
    user01 = da_client.query_create_address("user01")
    fee_collector = da_client.query_create_address("fee_collector", "remote")
    feeAllocate = da_client.query_create_address("feeAllocate", "remote")

    da_client.transfer_coin(dao, user01, "1000000")
    user01_balance = da_client.query_balance(user01)
    logger.info(f"user01_balance: {user01_balance}")

    feeAllocate_balance = da_client.query_balance(feeAllocate)
    logger.info(
        f"feeAllocate:{feeAllocate}, feeAllocate_balance: {feeAllocate_balance}")

    fees = "1000"
    da_client.transfer_coin(user01, dao, "1", fees)

    query_basic_params = da_client.execute(
        da_client.build("q", "feeAllocate", "basic-params"))
    allocate_rate = da_client.execute(
        da_client.build("q", "feeAllocate", "allocate-rate"))
    dev_operator_rate = allocate_rate["allocate_rate"]["dev_operator_rate"]
    fee_treasury_rate = allocate_rate["allocate_rate"]["fee_treasury_rate"]
    feeTreasuryAddress = query_basic_params["allocate_basic_param"]["fee_treasury_address"]
    devOperatorAddress = query_basic_params["allocate_basic_param"]["dev_operator_address"]
    allocatePeriod = query_basic_params["allocate_basic_param"]["allocation_period"]

    feeTreasuryAddress_balance = da_client.query_balance(feeTreasuryAddress)
    devOperatorAddress_balance = da_client.query_balance(devOperatorAddress)

    status = da_client.execute(da_client.build("status", ""))
    height = status.get("SyncInfo").get("latest_block_height")
    logger.info(f"height: {height}")
    total_amount = int(feeAllocate_balance["amount"]) + int(fees)
    logger.info(f"expect_total_amount: {total_amount}")
    while True:
        # +1区块 才会手续费才会分配至 feeAllocate, DA 出块时间较慢配置
        time.sleep(20)
        # 验证手续费被收取到了 fee_collector -> feeAllocate 地址
        feeAllocate_balance_after = da_client.query_balance(feeAllocate)
        status = da_client.execute(da_client.build("status", ""))
        height = status.get("SyncInfo").get("latest_block_height")
    
        logger.info(
            f"height:{height}, feeAllocate_balance_after: {feeAllocate_balance_after}")
        if feeAllocate_balance_after.get("amount") == "0":
            break
        if total_amount != int(feeAllocate_balance_after.get("amount")):
            total_amount = int(feeAllocate_balance_after.get("amount"))
            logger.info(
                f"There are other transactions happening, update total_amount: {total_amount}")

    feeTreasuryAddress_balance_after = da_client.query_balance(feeTreasuryAddress)
    devOperatorAddress_balance_after = da_client.query_balance(devOperatorAddress)

    fee_treasury_amount = int(total_amount * fee_treasury_rate / 100)

    dev_operator_amount = total_amount - fee_treasury_amount

    assert int(feeTreasuryAddress_balance_after["amount"]) - \
           int(feeTreasuryAddress_balance["amount"]) == fee_treasury_amount
    assert int(devOperatorAddress_balance_after["amount"]) - \
           int(devOperatorAddress_balance["amount"]) == dev_operator_amount


def test_allocate_period(da_client):
    """
    测试手续费分配周期
    - 1. 查询fee模块账户余额信息，普通用户发送交易，保持手续费账户有余额，等待分配
    - 2. 分配完后，查询分配周期参数，手动计算出下一个分配周期高度
    - 3. 发送一笔交易，验证手续费地址余额
    - 3. 查询当前区块高度 + 修改分配周期高度 < 下一个分配周期，立即结算
    - 4. 查询当前区块高度 + 修改分配周期高度 > 下一个分配周期，等待下一个分配周期高度结算
    - 5. 查询当前区块高度，比如更改超过已经过去5个区块，在此修改分配高度2
        - 步骤3 执行高度为100 -> 计算出来的分配高度为 100+100=200
        - 步骤4 当前高度为100+5 -> 计算出来的分配高度为 105 + 2=107
        - 107 < 200, 所以会交易成功后 +1 结算
    - 6. 按照步骤4的逻辑验证无误后，再次更新区块高度，将其区块高度结算值设置为大于的场景，等待最新结算高度验证手续费分配
    :param client:
    :return:
    """
    dao = da_client.query_create_address("dao")
    user02 = da_client.query_create_address("user02")
    feeAllocate = da_client.query_create_address("feeAllocate", "remote")
    da_client.transfer_coin(dao, user02, "1000000")
    fees = "1000"
    da_client.transfer_coin(user02, dao, "1", fees)

    allocate_rate = da_client.execute(
        da_client.build("q", "feeAllocate", "allocate-rate"))
    dev_operator_rate = allocate_rate["allocate_rate"]["dev_operator_rate"]
    fee_treasury_rate = allocate_rate["allocate_rate"]["fee_treasury_rate"]

    query_basic_params = da_client.execute(
        da_client.build("q", "feeAllocate", "basic-params"))
    feeTreasuryAddress = query_basic_params["allocate_basic_param"]["fee_treasury_address"]
    devOperatorAddress = query_basic_params["allocate_basic_param"]["dev_operator_address"]

    tx_resp = da_client.execute(da_client.build("tx", "feeAllocate",
                                          ["update-basic-params", feeTreasuryAddress, devOperatorAddress,
                                           20], **{"from": dao}))
    assert tx_resp["code"] == 0
    assert da_client.wait_for_tx_confirmation(tx_resp["txhash"])['code'] == 0

    query_basic_params = da_client.execute(
        da_client.build("q", "feeAllocate", "basic-params"))
    allocatePeriod = query_basic_params["allocate_basic_param"]["allocation_period"]

    # 1.等待分配
    while True:
        time.sleep(7)
        # 验证手续费被收取到了 fee_collector -> feeAllocate 地址
        feeAllocate_balance_after = da_client.query_balance(feeAllocate)
        logger.info(f"feeAllocate_balance_after: {feeAllocate_balance_after}")
        if feeAllocate_balance_after.get("amount") == "0":
            break
    height = da_client.execute(da_client.build("status", "")).get(
        "SyncInfo").get("latest_block_height")
    logger.info(f"height: {height}")

    # 计算下一个分配区块
    next_allocate_height = int(height) + int(allocatePeriod)
    logger.info(f"1.next_allocate_height: {next_allocate_height}")

    da_client.transfer_coin(user02, dao, "1", fees)

    time.sleep(10 * 3)  # 至少过去了3个区块
    feeAllocate_balance = da_client.query_balance(feeAllocate)
    logger.info(f"feeAllocate_balance: {feeAllocate_balance}")
    # 2.查询当前区块高度 + 修改分配周期高度 < 下一个分配周期，立即结算
    tx_resp = da_client.execute(da_client.build("tx", "feeAllocate",
                                          ["update-basic-params", feeTreasuryAddress, devOperatorAddress,
                                           3], **{"from": dao}))
    assert tx_resp["code"] == 0
    resp = da_client.wait_for_tx_confirmation(tx_resp["txhash"])
    resp['code'] == 0
    logger.info(f"update basic-params height: {resp["height"]}")
    next_allocate_height = int(resp["height"]) + int(3)
    logger.info(f"2.next_allocate_height: {next_allocate_height}")

    # 1.再次等待分配
    while True:
        time.sleep(7)
        # 验证手续费被收取到了 fee_collector -> feeAllocate 地址
        feeAllocate_balance_after = da_client.query_balance(feeAllocate)
        logger.info(f"feeAllocate_balance_after: {feeAllocate_balance_after}")
        if feeAllocate_balance_after.get("amount") == "0":
            break
    height = da_client.execute(da_client.build("status", "")).get(
        "SyncInfo").get("latest_block_height")
    logger.info(f"height: {height}")

    assert int(height) < next_allocate_height

    da_client.transfer_coin(user02, dao, "1", fees)

    # 3.查询当前区块高度 + 修改分配周期高度 > 下一个分配周期，等待下一个分配周期高度结算
    tx_resp = da_client.execute(da_client.build("tx", "feeAllocate",
                                          ["update-basic-params", feeTreasuryAddress, devOperatorAddress,
                                           20], **{"from": dao}))
    assert tx_resp["code"] == 0
    resp = da_client.wait_for_tx_confirmation(tx_resp["txhash"])
    assert resp['code'] == 0

    logger.info(f"update basic-params height: {resp["height"]}")
    next_allocate_height = int(height) + int(allocatePeriod)
    logger.info(f"3.next_allocate_height: {next_allocate_height}")

    while True:
        time.sleep(7)
        # 验证手续费被收取到了 fee_collector -> feeAllocate 地址
        feeAllocate_balance_after = da_client.query_balance(feeAllocate)
        logger.info(f"feeAllocate_balance_after: {feeAllocate_balance_after}")
        if feeAllocate_balance_after.get("amount") == "0":
            break
    height = da_client.execute(da_client.build("status", "")).get(
        "SyncInfo").get("latest_block_height")
    logger.info(f"height: {height}")

    assert int(height) >= next_allocate_height

    pass
