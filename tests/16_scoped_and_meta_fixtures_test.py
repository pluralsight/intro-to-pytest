from pytest import fixture, mark


@fixture(scope="module")
def module_fixture():
    """
    Scoping affects how often fixtures are (re)initialized
    """
    print "\n(begin module_fixture)"
    yield
    print "\n(end module_fixture)"


def test_scoped_fixtures_1(module_fixture):
    print "\n   Running test_scoped_fixtures_1"


def test_scoped_fixtures_2(module_fixture):
    print "\n   Running test_scoped_fixtures_2"


@fixture()
def meta_fixture():
    print '\n*** begin meta_fixture ***'
    yield
    print '\n*** end meta_fixture ***'

# # Uncomment me to really "get meta"
# pytestmark = mark.usefixtures("meta_fixture")

# How could we get meta_fixture to only run once?
