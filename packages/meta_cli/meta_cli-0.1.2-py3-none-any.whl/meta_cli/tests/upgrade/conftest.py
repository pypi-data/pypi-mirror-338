import pytest

from meta_cli.core.command_builder import ChainClientFactory, ChainClient


uat4_config_path = "./config/uat4_247/chains.yml"
uat1_config_path = "./config/uat1_204/chains.yml"




@pytest.fixture(scope="module")
def me_client_v2():
    factory = ChainClientFactory(uat4_config_path)
    config = factory.get_config("me-hub")
    return ChainClient(config)


@pytest.fixture(scope="module")
def me_client_v1():
    factory = ChainClientFactory(uat1_config_path)
    config = factory.get_config("me-hub")
    return ChainClient(config)
