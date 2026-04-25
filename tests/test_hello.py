from example_private_lib import hello


def test_hello():
    assert hello() == "Hello from example-private-lib!"
