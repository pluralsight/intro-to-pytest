import pytest


@pytest.mark.parametrize("number", [1, 2, 3, 4, 5])
def test_numbers(number):
    """
    mark can be used to apply "inline" parameterization, without a fixture
    """
    print("\nRunning test_numbers with {}".format(number))


@pytest.mark.parametrize("x, y", [(1, 1), (1, 2), (2, 2)])
def test_dimensions(x, y):
    """
    mark.parametrize can even unpack tuples into named parameters
    """
    print("\nRunning test_coordinates with {}x{}".format(x, y))

@pytest.mark.parametrize("mode", [1, 2, 3], ids=['foo', 'bar', 'baz'])
def test_modes(mode):
    """
    The `ids` kwarg can be used to rename the parameters
    """
    print("\nRunning test_modes with {}".format(mode))
