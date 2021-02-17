import myproject.web
import pytest


@pytest.mark.integration
def test_web_server():
    from multiprocessing import Process
    from time import sleep
    import os
    import signal

    p = Process(target=myproject.web.server)
    p.start()
    assert p.pid != 0
    sleep(2)
    os.kill(p.pid, signal.SIGKILL)
    p.join(timeout=2)


@pytest.mark.integration
def test_web_health(client):
    r = client.get('/health')

    assert r.status == "200 OK"
