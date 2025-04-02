import pytest

from meta_cli.core.command_builder import ChainClientFactory, ChainClient

# config_path = "./config/dev1_198/chains.yml"
# config_path = "./config/uat3_248/chains.yml"
config_path = "./config/uat4_247/chains.yml"


@pytest.fixture(scope="module")
def da_client() -> ChainClient:
    """共享的Celestia客户端实例，模块级复用"""
    factory = ChainClientFactory(config_path)
    config = factory.get_config("celestia")
    return ChainClient(config)


@pytest.fixture(scope="module")
def me_client() -> ChainClient:
    """共享的me客户端实例，模块级复用"""
    factory = ChainClientFactory(config_path)
    config = factory.get_config("me-hub")
    return ChainClient(config)


@pytest.fixture(scope="module")
def rollup_client() -> ChainClient:
    """共享的rollup客户端实例，模块级复用"""
    factory = ChainClientFactory(config_path)
    config = factory.get_config("rollup")
    return ChainClient(config)


@pytest.fixture
def is_dev(me_client):
    return "dev" in me_client.home_dir
