from other_code.services import count_service
from pytest import fixture, raises


@fixture
def re_usable_db_mocker(mocker):
    """
    Fixtures can invoke mocker to yield "re-usable" mocks
    """
    mock_db_service = mocker.patch("other_code.services.db_service", autospec=True)
    mock_db_service.return_value = [(0, "fake row", 0.0)]
    return mock_db_service


def test_re_usable_mocker(re_usable_db_mocker):
    c = count_service("foo")
    re_usable_db_mocker.assert_called_with("foo")
    assert c == 1


def test_mocker_with_exception(re_usable_db_mocker):
    re_usable_db_mocker.side_effect = Exception("Oh noes!")

    with raises(Exception):
        count_service("foo")
