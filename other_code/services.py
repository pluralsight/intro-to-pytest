import time
from collections import namedtuple


class ExpensiveClass(object):
    """
    A fake Class that takes a long time to fully initialize
    """

    def __init__(self):
        print("(Initializing ExpensiveClass instance...)")
        time.sleep(0.2)
        print("(ExpensiveClass instance complete!)")


FakeRow = namedtuple("FakeRow", ("id", "name", "value"))


def db_service(query_parameters):
    """
    A fake DB service that takes a remarkably long time to yield results
    """
    print("(Doing expensive database stuff!)")

    time.sleep(5.0)

    data = [FakeRow(0, "Foo", 19.95), FakeRow(1, "Bar", 1.99), FakeRow(2, "Baz", 9.99)]

    print("(Done doing expensive database stuff)")
    return data


def count_service(query_parameters):
    print("count_service: Performing a query (and counting the results)...")

    data = db_service(query_parameters)

    count = len(data)

    print("Found {} result(s)!".format(count))
    return count


DATA_SET_A = {
    "Foo": "Bar",
    "Baz": [5, 7, 11],
    "Qux": {"A": "Boston", "B": "Python", "C": "TDD"},
}

DATA_SET_B = DATA_SET_A

DATA_SET_C = {
    "Foo": "Bar",
    "Baz": [3, 5, 7],
    "Qux": {"A": "Boston", "B": "Python", "C": "TDD"},
}
