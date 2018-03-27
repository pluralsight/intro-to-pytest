from pytest import fixture


def safe_cleanup():
    print "\n(Running safe_cleanup, even if the fixture failed...)"


def risky_function():
    pass
    # # Uncomment to simulate a failure during Fixture setup!
    # raise Exception("Whoops, I guess that risky function didn't work...")


@fixture
def safe_cleanup_fixture(request):
    """
    The request can also be used to apply post-test callbacks
    """
    request.addfinalizer(safe_cleanup)

    risky_function()

    assert True


def test_with_safe_cleanup_fixture(safe_cleanup_fixture):
    print "\n\nRunning test_with_safe_cleanup_fixture..."
    assert True
