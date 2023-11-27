import pytest


def test_with_yield_fixture(yield_fixture):
    print("\n    Running test_with_yield_fixture: {}".format(yield_fixture))
    assert "foo" in yield_fixture


@pytest.fixture
def yield_fixture():
    """
    Fixtures can yield their data
    (additional code will run after the test)
    """
    print("\n\n(Initializing yield_fixture)")
    x = {"foo": "bar"}

    # Remember, unlike generators, fixtures should only yield once (if at all)
    yield x

    print("\n(Cleaning up yield_fixture)")
    del(x)
