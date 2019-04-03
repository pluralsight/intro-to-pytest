import pytest

dev_s3_credentials = None


@pytest.mark.skip
def test_broken_feature():
    # Always skipped!
    assert False


@pytest.mark.skipif(not dev_s3_credentials, reason="S3 creds not found!")
def test_s3_api():
    # Skipped if a certain condition is met
    assert True


@pytest.mark.xfail
def test_where_failure_is_acceptable():
    # Allows failed assertions (returns "XPASS" if there are no failures)
    assert True


@pytest.mark.xfail
def test_where_failure_is_accepted():
    # Allows failed assertions (returns "xfail" on failure)
    assert False


@pytest.mark.xfail(strict=True)
def test_where_failure_is_mandatory():
    # Requires failed assertions! (returns "xfail" on failure; FAILs on pass!)
    assert True


# # Uncomment to skip everything in the module
# pytest.skip("This whole Module is problematic at best!", allow_module_level=True)
