import pytest
import os

from pylotus_rpc.methods.net import _addrs_listen, _peers, _agent_version, _auto_nat_status
from pylotus_rpc.http_json_rpc_connector import HttpJsonRpcConnector

@pytest.fixture
def connector():
    host = os.environ.get('LOTUS_GATEWAY', 'https://filfox.info/rpc/v0')
    return HttpJsonRpcConnector(host=host)

@pytest.mark.integration
def test_auto_nat_status(connector):
    result = _auto_nat_status(connector)
    assert result is not None
    assert result.reachability == 1
    assert result.public_addrs is not None
    assert len(result.public_addrs) > 0

@pytest.mark.integration
def test_agent_version(connector):
    peers = _peers(connector)
    result = _agent_version(connector, peers[0].peer_id)
    assert result is not None
    assert len(result) > 0

@pytest.mark.integration
def test_addrs_listen(connector):
    result = _addrs_listen(connector)
    assert result is not None
    
@pytest.mark.integration
def test_peers(connector):
    result = _peers(connector)
    assert result is not None
    assert len(result) > 0
