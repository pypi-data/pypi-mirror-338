from pickletools import pyset
from loguru import logger
import pytest

from meta_cli.core.command_builder import ChainClient
from meta_cli.core import common_assert as ca
from meta_cli.tests.conftest import me_client


def test_me_ibc_transfer(da_client, me_client):
    SOURCE_EVENT_QUERY = "tm.event='Tx' AND message.action='/ibc.core.channel.v1.MsgAcknowledgement'"
    to_address = da_client.query_create_address("dao")
    from_name = "global_dao"
    user1 = me_client.execute(me_client.build("keys", "show", from_name))
    from_address = user1["address"]
    amount = 10000000000
    fees = 4000

    balance = me_client.execute(me_client.build("query", "bank", "balances", from_address,
                                                **{"denom": "umec"}))
    resp = me_client.execute(me_client.build("tx", "ibc-transfer",
                                             ["transfer", "transfer", f"{me_client.channels["to_celestia"]}",
                                              f"{to_address}", f"{amount}umec"],
                                             **{"from": f"{from_address}", "fees": f"{fees}umec"}))
    tx_receipt = ca.assert_tx_success(me_client, resp)
    logger.info(f"tx_receipt:{tx_receipt}")
    balance1 = me_client.execute(me_client.build("query", "bank", "balances", from_address,
                                                 **{"denom": "umec"}))

    resp = me_client.sync_subscribe(SOURCE_EVENT_QUERY)
    logger.info(f"监听到对应事件: {resp}")

    # global_dao Free transaction fees, but uat global_dao != super
    if "dev" in da_client.home_dir:
        assert int(balance1["amount"]) == int(balance["amount"]) - amount
    else:
        assert int(balance1["amount"]) == int(
            balance["amount"]) - amount - fees


def test_super_admin_tx(me_client: ChainClient, is_dev):
    if is_dev:
        pytest.skip("skip dev")
    cmd = me_client.build("tx", "staking", ["stake",
                                            "mevaloper1a9mhtl64780lf4m688clez83wugftuedkprsr8",
                                            f"100000000{me_client.denom}"],
                          **{"from": "super", "gas": f"500000"})
    file_path = "tx.json"
    cmd += f" --generate-only > {file_path}"
    print("cmd---------", cmd)
    resp = me_client.execute(cmd)
    print("resp--------", resp)
    assert resp.get("raw") == ''
    resp = me_client.hub_super_sign(file_path)
    logger.info(resp)
    pass
