from pytest import fixture, skip
import string


@fixture(params=['a', 'b', 'c'])
def letters_fixture(request):
    yield request.param


@fixture(params=[1, 2, 3, 4])
def coordinates_fixture(request, letters_fixture):
    """
    Fixtures can invoke each other (producing cartesian products of params)
    """
    coordinate = letters_fixture + str(request.param)
    yield coordinate
    # # Uncomment for fun 80s board game reference
    # if coordinate == 'b2':
    #     print "(Don't sink my Battleship!)"
    #     skip()


def test_fixtureception(coordinates_fixture):
    print "\nRunning test_fixtureception with \"{}\"".format(
        coordinates_fixture)
    assert len(coordinates_fixture) == 2
