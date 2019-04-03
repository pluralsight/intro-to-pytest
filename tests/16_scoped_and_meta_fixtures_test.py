from pytest import fixture, mark
from other_code.services import ExpensiveClass


@fixture(scope="module", autouse=True)
def scoped_fixture():
    """
    Scoping affects how often fixtures are (re)initialized
    """
    print("\n(Begin Module-scoped fixture)")
    yield ExpensiveClass()
    print("\n(End Module-scoped fixture)")


@mark.parametrize("x", range(1, 51))
def test_scoped_fixtures(x):
    """
    A (hopefully fast!) test, to be run with fifty different parameters...
    """
    print("\n   Running test_scoped_fixture")
