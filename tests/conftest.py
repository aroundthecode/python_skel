import urllib3
import pytest
import myproject.web

urllib3.disable_warnings()


@pytest.fixture()
def client():

    if myproject.web.webapp is None:
        myproject.web.init_webapp()
        myproject.web.webapp.config['TESTING'] = True
        myproject.web.api_importer()
    client = myproject.web.webapp.test_client()

    yield client
