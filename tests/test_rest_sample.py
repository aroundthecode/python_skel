import pytest


@pytest.mark.integration
def test_web_info(client):
    r = client.get('/sample/me/')
    assert r.status == "200 OK"
    assert r.data.decode('utf-8') == "\"Hello me\""
