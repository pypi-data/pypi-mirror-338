from loguru import logger

from meta_cli.core.command_builder import ChainClient


def test_da_ibc_transfer(da_client: ChainClient, me_client: ChainClient):
    SOURCE_EVENT_QUERY = "tm.event='Tx' AND message.action='/ibc.core.channel.v1.MsgAcknowledgement'"
    da_dao = da_client.query_create_address("dao")
    me_global_dao = me_client.query_create_address("global_dao")
    amount = 10000
    fees = 4000

    da_dao_balance = da_client.query_balance(da_dao)
    logger.info(f"da_dao_balance: {da_dao_balance}", )

    me_global_dao_balance = me_client.query_balance(me_global_dao)
    logger.info(f"me_global_dao_balance: {me_global_dao_balance}", )

    resp = da_client.execute(da_client.build("tx", "ibc-transfer",
                                       ["transfer", "transfer", f"{da_client.channels["to_me"]}",
                                        f"{me_global_dao}", f"{amount}{da_client.denom}"],
                                       **{"from": f"{da_dao}", "fees": f"{fees}{da_client.denom}"}))
    resp2 = da_client.wait_for_tx_confirmation(resp["txhash"])
    logger.info(resp2)

    resp = da_client.sync_subscribe(SOURCE_EVENT_QUERY)
    logger.info(f"监听到对应事件: {resp}")

    me_global_dao_balance_after = me_client.query_balance(me_global_dao)
    da_dao_balance_after = da_client.query_balance(da_dao)

    assert int(me_global_dao_balance_after["amount"]) == int(me_global_dao_balance["amount"]) + int(
        amount), "from_address金额验证错误"
    # da_dao Free transaction fees
    assert int(da_dao_balance_after["amount"]) == int(da_dao_balance["amount"]) - int(amount), "to_address金额验证错误"
