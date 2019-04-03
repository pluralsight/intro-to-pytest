from pytest import fixture, mark
from other_code.services import ExpensiveClass


@fixture(scope="module")
def scoped_fixture():
    """
    Scoping affects how often fixtures are (re)initialized
    """
    print("\n(begin scoped_fixture)")
    yield ExpensiveClass()
    print("\n(end scoped_fixture)")


@mark.parametrize("x", range(1, 51))
def test_scoped_fixtures(x, scoped_fixture):
    """
    A (hopefully fast!) test, to be run with fifty different parameters...
    """
    print("\n   Running test_scoped_fixtures")
