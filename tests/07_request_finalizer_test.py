import pytest


def test_with_safe_cleanup_fixture(safe_fixture):
    print("\nRunning test_with_safe_cleanup_fixture...")
    assert True


@pytest.fixture
def safe_fixture(request):
    """
    The request can also be used to apply post-test callbacks
    (these will run even if the Fixture itself fails!)
    """
    print("\n(Begin setting up safe_fixture)")
    request.addfinalizer(safe_cleanup)
    risky_function()


def safe_cleanup():
    print("\n(Cleaning up after safe_fixture!)")


def risky_function():
    # # Uncomment to simulate a failure during Fixture setup!
    # raise Exception("Whoops, I guess that risky function didn't work...")
    print("   (Risky Function: Totally worth it!)")
