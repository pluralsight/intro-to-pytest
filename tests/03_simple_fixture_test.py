from pytest import fixture


@fixture
def simple_fixture():
    """
    Fixtures are callables decorated with @fixture
    """
    print "\n(Doing Setup Stuff!)"


def test_with_simple_fixture(simple_fixture):
    """
    They can be invoked simply by having a positional arg with the same name!
    """
    print "Running test_with_simple_fixture..."
    assert True


def test_also_with_simple_fixture(simple_fixture):
    print "Running test_also_with_simple_fixture..."
    assert True
