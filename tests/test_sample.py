from myproject.backend.sample import hello


def test_hello():

    ret = hello("me")
    assert ret == "Hello me"
