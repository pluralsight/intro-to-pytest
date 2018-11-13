from pytest import fixture


@fixture
def introspective_fixture(request):
    """
    The request fixture allows introspection into the "requesting" test
    """
    print "\n\nintrospective_fixture:"
    print "    Called at {}-level scope".format(request.scope)
    print "    On the {} node".format(request.node)
    print "    In the {} module".format(request.module)


def test_with_introspective_fixture(introspective_fixture):
    print "\nRunning test_with_introspective_fixture..."
    assert True
