from pytest import fixture


@fixture
def one_fixture():
    """
    Beyond just "doing stuff", fixtures can return data
    """
    print "\n(Returning 1 from data_fixture)"
    return 1


def test_with_data_fixture(one_fixture):
    """
    The fixture "argument" will contain the returned data
    """
    print "\nRunning test_with_data_fixture: {}".format(one_fixture)
    assert one_fixture == 1
