from pytest import fixture


def safe_cleanup():
    print "\n(Running safe_cleanup! Even if the fixture failed...)"


def risky_function():
    pass
    # # Uncomment to simulate a failure during Fixture setup!
    # raise Exception("Whoops, I guess that risky function didn't work...")
    # print "   (Risky Function: Totally worth it!)"


@fixture
def safe_fixture(request):
    """
    The request can also be used to apply post-test callbacks
    (these will run even if the Fixture itself fails!)
    """
    print "\n(Starting safe_fixture setup)"

    request.addfinalizer(safe_cleanup)

    risky_function()

    print "(Finishing safe_fixture setup)"


def test_with_safe_cleanup_fixture(safe_fixture):
    print "\nRunning test_with_safe_cleanup_fixture..."
    assert True
