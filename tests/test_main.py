from myproject.main import hello


def test_hello():

    ret = hello()
    assert ret == "Hello"
