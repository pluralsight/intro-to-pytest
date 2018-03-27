import time
from collections import namedtuple

FakeRow = namedtuple('FakeRow', ('id', 'name', 'value'))


def db_service(query_parameter):
    print "(Doing crazy database stuff!)"

    time.sleep(1.5)

    data = [
        FakeRow(0, "Foo", 19.95),
        FakeRow(1, "Bar", 1.99),
        FakeRow(2, "Baz", 9.99),
    ]

    print "(Ok, done doing crazy database stuff)"
    return data


def count_service(query_parameter):
    print "Getting a query so we can count the results..."

    data = db_service(query_parameter)

    count = len(data)

    print "Found {} result(s)!".format(count)
    return count
