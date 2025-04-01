import random
import string
from typing import Any

import pytest
from loguru import logger

from meta_cli.core.command_builder import ChainClient
from meta_cli.tests.conftest import client, me_client, rollup_client
from meta_cli.core import common_assert as ca


@pytest.mark.usefixtures("client", "me_client", "rollup_client")
class TestKyc:
    da_client = None
    me_client = None
    rollup_client = None

    @pytest.fixture(autouse=True)
    def inject_tester(self, client: ChainClient, me_client: ChainClient, rollup_client: ChainClient):
        self.da_client = client
        self.me_client = me_client
        self.rollup_client = rollup_client

    @classmethod
    def create_instance(cls, da_client, me_client, rollup_client):
        """创建一个已初始化的 TestKyc 实例，用于其他测试类"""
        instance = cls()
        instance.da_client = da_client
        instance.me_client = me_client
        instance.rollup_client = rollup_client
        return instance

    def test_kyc(self, address: str = None, region_id: str = "chn") -> tuple[str | Any, Any]:
        if address is None:
            name = "user-" + \
                ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            address = self.me_client.query_create_address(name)
            logger.info(address)

        global_dao = self.me_client.query_create_address("global_dao")
        did = str(random.randint(10 ** 12, 10 ** 13 - 1))
        region_id = region_id
        pubkey = '{\"key\":\"A19MEo0JwANGK2hSJiUGwa/FWI8ElIfSAAG2iogl2RDr\"}'
        level = '2'
        uri = "https://baidu.com"
        hash = "536DD344E00C1194B7C08FAE4CCC8CDBA61AD6EA"
        inviter = global_dao

        cmd = self.me_client.build("tx", "kyc",
                                   ["approve", did, region_id, address,
                                       pubkey, level, uri, hash, inviter],
                                   **{"from": "super", "gas": "500000"})
        file_path = "tx.json"
        cmd += f" --generate-only > {file_path}"
        resp = self.me_client.execute(cmd)
        assert resp.get("raw") == ''
        resp = self.me_client.hub_super_sign(file_path)
        tx_receipt = ca.assert_tx_success(self.me_client, resp)
        logger.info(tx_receipt)
        return address, tx_receipt
