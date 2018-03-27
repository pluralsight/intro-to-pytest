from pytest import fixture
import string


@fixture(params=['a', 'b', 'c'])
def letters_fixture(request):
    """
    Fixtures with parameters will run once per param (via request)
    """
    yield request.param


def test_parameterization(letters_fixture):
    print "\nRunning test_parameterized_fixture with parameter {}".format(
        letters_fixture)

    assert letters_fixture in string.ascii_letters
