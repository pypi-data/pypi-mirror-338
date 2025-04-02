import os
import subprocess
import time
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Literal, Any, Union
import asyncio
import json
from websockets import connect

import yaml
from loguru import logger

from meta_cli.utils import decode_base64


class ChainClientFactory:
    def __init__(self, config_path):
        self.config = self._load_config(config_path)
        self.config_keys = self.get_config_keys()

    def _load_config(self, config_path):
        with open(config_path) as f:
            return yaml.safe_load(f)

    def get_config_keys(self):
        """获取配置文件中的链名"""
        return list(self.config.keys()) if self.config else []

    def get_config(self, chain):
        if chain not in self.config:
            raise Exception(f"未找到链{chain}的配置")
        return self.config[chain]


class BaseChainClient:
    def __init__(self, chain):
        self.cli_path = chain["cli_path"]
        self.chain_id = chain["chain_id"]
        self.home_dir = chain["home_dir"]
        self.node_rpc = chain["node_rpc"]
        self.node_ws_url = chain["node_ws_url"]
        self.modules = chain["modules"]
        self.channels = chain["channels"]
        self.denom = chain["base_denom"]
        self.command = None

        self.thread_pool_executor = ThreadPoolExecutor()

    def build(self, action, module, *args, **kwargs):
        base_cmd = f"{self.cli_path} {action} {module}"
        if action == "tx":
            global_cmd = f"--chain-id {self.chain_id} --home {self.home_dir} --keyring-backend=test -y --node {self.node_rpc} --output json"
        elif action in ("query", "q"):
            global_cmd = f"--home {self.home_dir} --node {self.node_rpc} --output json"
            if self.cli_path != "me-chaind":
                global_cmd += f" --chain-id {self.chain_id}"
        elif action in "keys":
            global_cmd = f"--home {self.home_dir} --keyring-backend=test --output json"
        else:
            global_cmd = f"--node {self.node_rpc}"
        flattened_args = []
        for arg in args:
            if isinstance(arg, (list, tuple)):
                flattened_args.extend(map(str, arg))
            else:
                flattened_args.append(str(arg))
        arg_params = " ".join(flattened_args)
        kw_params = " ".join([f"--{k} {v}" for k, v in kwargs.items()])
        self.command = f"{base_cmd} {arg_params} {kw_params} {global_cmd}"
        return self.command

    def execute(self, cmd):
        try:
            logger.info(f"executing command: {cmd}")
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                check=True,
                env=os.environ.copy()
            )
            if result.returncode == 0 and result.stdout == "":
                return self._parse_output(result.stderr)
            return self._parse_output(result.stdout)
        except subprocess.CalledProcessError as e:
            error_msg = f"Command failed ({e.returncode}), STDOUT: {e.stdout}\nSTDERR: {e.stderr}"
            logger.trace(error_msg)
            return self._parse_output(error_msg)

    def _parse_output(self, raw):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {"raw": raw}


class MEClient(BaseChainClient):
    def __init__(self, chain):
        super().__init__(chain)

    def get_regions(self, region_id: str = None):
        if region_id:
            region = self.execute(self.build(
                "query", "staking", "region", region_id))
        else:
            region = self.execute(self.build("query", "staking", "regions"))
        return region

    def region_exists(self, region_id):
        """判断区域是否在链上存在"""
        regions: Union[list, None] = self.get_regions().get("region", None)
        region_ids = []
        if regions is not None:
            region_ids = [region['regionId'] for region in regions]
        return region_id in region_ids

    def get_fixed_deposit(self, id: Union[str, int] = None, amount=False):
        """
        获取用户的定期存款
        Args:
            id: 用户地址 or id
            amount: 是否查询定期存款金额
        Returns:
            定期存款列表
        """
        if isinstance(id, str):
            address = id
            if amount:
                fixed_info = self.execute(self.build(
                    "query", "staking", "show-fixed-deposit-amount-by-acct", address))
            else:
                fixed_info = self.execute(self.build(
                    "query", "staking", "show-fixed-deposit-by-acct", address))

        elif isinstance(id, int):
            # 如果 id 是整数，查询特定 ID 的固定存款
            fixed_info = self.execute(self.build(
                "query", "staking", "show-fixed-deposit", id))
        else:
            # 如果未提供 id 或 id 类型不符合上述条件，列出所有固定存款
            fixed_info = self.execute(self.build(
                "query", "staking", "list-fixed-deposit"))
        return fixed_info


class DAClient(BaseChainClient):
    def __init__(self, chain):
        super().__init__(chain)


class RollupClient(BaseChainClient):
    def __init__(self, chain):
        super().__init__(chain)


class ChainClient(MEClient, DAClient, RollupClient):

    def wait_for_tx_confirmation(
            self,
            tx_hash: str,
            timeout: int = 30,
            interval: int = 5
    ) -> Dict:
        start_time = time.time()

        while (time.time() - start_time) < timeout:
            time.sleep(interval)
            response = self.execute(self.build("query", "tx", tx_hash))
            if "not found" in response.get("raw", ""):
                continue

            if response.get("code") is not None and response.get("height"):
                return response

        logger.error(f"TxHash Timeout: {tx_hash}")
        return {}

    def query_create_address(self, name, target: Literal["local", "remote"] = "local"):
        if target == "local":
            user_info = self.execute(self.build("keys", "show", name))
            if isinstance(user_info, dict) and user_info.get("address"):
                return user_info["address"]
            address = self.execute(
                "echo y | " + self.build("keys", "add", name))["address"]
            return address
        if target == "remote":
            # support remote ModuleAccount query
            module_account = self.execute(self.build(
                "query", "auth", "module-account", name))
            if isinstance(module_account, dict):
                return module_account.get("account").get("base_account").get("address")
            pass

    def transfer_coin(self, from_address, to_address, amount: str, fees: str = 0, denom: str = None):
        if not denom:
            denom = self.denom
        transfer_resp = self.execute(
            self.build("tx", "bank", ["send", from_address, to_address, str(amount) + denom],
                       **{"from": from_address, "fees": str(fees) + denom}))
        assert transfer_resp["code"] == 0
        assert self.wait_for_tx_confirmation(
            transfer_resp["txhash"])["code"] == 0

    def query_balance(self, address, denom=None):
        if not denom:
            denom = self.denom
        return self.execute(self.build("query", "bank", "balances", address, **{"denom": denom}))

    # 等待到指定区块高度
    def wait_for_block_height(self, height: int, timeout: int = 20, interval: int = 7):
        start_time = time.time()

        while (time.time() - start_time) < timeout:
            time.sleep(interval)
            response = self.execute(self.build("status", ""))
            if response.get("SyncInfo").get("latest_block_height") >= height:
                return response

        logger.error(f"Block Height Timeout: {height}")
        return {}

    def hub_super_sign(self, file_path: str):
        if self.cli_path != "med":
            logger.error("Only me-hub can use this function")
            return None
        super_addr = self.query_create_address("super")
        signed_path = []
        for i in range(1, 4):
            sign_cmd = self.build("tx", "sign", file_path,
                                  **{"from": f"u{i}", "multisig": super_addr})
            sign_cmd += f" > tx-signed-u{i}.json"
            resp = self.execute(sign_cmd)
            assert resp.get("raw") == ''
            signed_path.append(f"tx-signed-u{i}.json")
        multisign_cmd = self.build(
            "tx", "multisign", file_path, "super", *signed_path)
        multisign_cmd += f" > tx-signed-super.json"
        self.execute(multisign_cmd)
        broadcast_cmd = self.build("tx", "broadcast", "./tx-signed-super.json")
        return self.execute(broadcast_cmd)

    def sync_subscribe(self, query):
        """同步化封装异步监听"""
        future = self.thread_pool_executor.submit(
            asyncio.run,  # 在新线程运行协程
            self.subscribe_event(query))
        return future.result()

    async def subscribe_event(self, event_query: str = None):

        async with connect(self.node_ws_url) as websocket:
            # 发送订阅请求
            sub_request = {"jsonrpc": "2.0", "method": "subscribe",
                           "params": {"query": event_query}, "id": 1}
            await websocket.send(json.dumps(sub_request))

            while True:
                try:
                    response = await websocket.recv()
                    data = json.loads(response)

                    if "result" in data and "data" in data["result"]:
                        event_data = data["result"]["data"]
                        if event_data["type"] == "tendermint/event/Tx":
                            tx_result = event_data["value"]["TxResult"]
                            event_fields = event_data["value"]["TxResult"]["result"]['events']

                            attrs = decode_base64.decode_base64_fields(
                                event_fields)
                            # "hash": tx["txHash"],  clid tx decode tx_result["tx"]
                            ibc_packet = {"height": tx_result["height"],
                                          "sender": _find_attribute(attrs, "sender"),
                                          "receiver": _find_attribute(attrs, "receiver"),
                                          "denom": _find_attribute(attrs, "denom"),
                                          "amount": _find_attribute(attrs, "amount")}
                            print(
                                f"捕获 IBC 交易: {json.dumps(ibc_packet, indent=2)} ")
                            return ibc_packet
                except Exception as e:
                    print(f"处理错误:{str(e)}")
                    break


def _find_attribute(tx_data, key):
    """从事件属性中提取特定值"""
    if isinstance(tx_data, dict):
        for attr in tx_data.get("attributes", []):
            if attr["key"] == key:
                return attr["value"]

            # 递归查找嵌套的字典或列表
            for v in tx_data.values():
                result = _find_attribute(v, key)
                if result is not None:
                    return result

    if isinstance(tx_data, list):
        for item in tx_data:
            result = _find_attribute(item, key)
            if result is not None:
                return result

    return None


if __name__ == "__main__":
    factory = ChainClientFactory("./config/uat4_247/chains.yml")
    config = factory.get_config("me-hub")
    client = ChainClient(config)

    resp = client.get_regions()
    print(resp)
    resp2 = client.region_exists("abc")
    print(resp2)
    pass

    # client.transfer_coin(client.query_create_address("dao"),
    #                      client.query_create_address("no_dao"), "11", "10000")

    # DESTINATION_EVENT_QUERY = "tm.event='Tx' AND message.action='/ibc.core.channel.v1.MsgRecvPacket'"
    # SOURCE_EVENT_QUERY = "tm.event='Tx' AND message.action='/ibc.core.channel.v1.MsgAcknowledgement'"
    # asyncio.run(client.subscribe_event(SOURCE_EVENT_QUERY))
