from pytest import fixture, mark


@fixture(scope="module")
def meta_fixture():
    print("\n*** begin meta_fixture ***")
    yield
    print("\n*** end meta_fixture ***")


# Apply this fixture to everything in this module!
pytestmark = mark.usefixtures("meta_fixture")


def test_with_meta_fixtures_a():
    print("\n   Running test_with_meta_fixtures_a")


def test_with_meta_fixtures_b():
    print("\n   Running test_with_meta_fixtures_b")


# How could we tell meta_fixture to only run once, "around" our tests?
# (See 16_scoped_and_meta_fixtures_test.py for a hint...)
