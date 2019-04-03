from __future__ import print_function
from pytest import fixture


@fixture
def global_fixture():
    print("\n(Doing global fixture setup stuff!)")
