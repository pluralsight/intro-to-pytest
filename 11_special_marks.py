import pytest

dev_s3_credentials = None


@pytest.mark.skip
def test_broken_feature():
    assert False


@pytest.mark.skipif(not dev_s3_credentials, reason="S3 creds not found!")
def test_s3_api():
    assert True


@pytest.mark.xfail
def test_where_failure_is_acceptable():
    assert True


@pytest.mark.xfail
def test_where_failure_is_accepted():
    assert False


@pytest.mark.xfail(strict=True)
def test_where_failure_is_mandatory():
    assert False

# Uncomment to skip everything in the module
#pytest.skip("This whole Module is crap!", allow_module_level=True)
