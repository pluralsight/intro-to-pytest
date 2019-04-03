import pytest
import string


def test_parameterization(letter):
    print("\n   Running test_parameterization with {}".format(letter))
    assert letter in string.ascii_letters


@pytest.fixture(params=["a", "b", "c", "d", "e"])
def letter(request):
    """
    Fixtures with parameters will run once per param
    (You can access the current param via the request fixture)
    """
    yield request.param
