from pytest import fixture, skip


@fixture(params=[1, 2, 3, 4])
def numbers_fixture(request):
    """
    Fixtures can cause tests to be run multiple times (once per parameter)
    """
    yield request.param


@fixture(params=['a', 'b', 'c', 'd'])
def coordinates_fixture(request, numbers_fixture):
    """
    Fixtures can invoke each other (producing cartesian products of params)
    """
    coordinate = request.param + str(numbers_fixture)
    yield coordinate
    # Uncomment for fun 80s board game reference (and fixture filtering)
    if coordinate == 'b2':
        print "\n(Don't sink my Battleship!)"
        skip()


def test_advanced_fixtureception(coordinates_fixture):
    print "\nRunning test_advanced_fixtureception with \"{}\"".format(
        coordinates_fixture)
