import pytest
from typing import TypeVar, Type
from meta_cli.core.command_builder import ChainClient

T = TypeVar('T', bound='BaseChainTest')


class BaseChainTest:
    """
    所有链相关测试的基类，提供通用fixture注入和实例创建逻辑
    """
    da_client: ChainClient = None
    me_client: ChainClient = None
    rollup_client: ChainClient = None

    @pytest.fixture(autouse=True)
    def inject_clients(self, da_client: ChainClient, me_client: ChainClient, rollup_client: ChainClient):
        """自动注入所有测试类需要的客户端"""
        self.da_client = da_client
        self.me_client = me_client
        self.rollup_client = rollup_client

    @classmethod
    def create_instance(cls: Type[T], da_client: ChainClient, me_client: ChainClient, rollup_client: ChainClient) -> T:
        """所有子类通用的实例创建方法"""
        instance = cls()
        instance.da_client = da_client
        instance.me_client = me_client
        instance.rollup_client = rollup_client
        return instance
