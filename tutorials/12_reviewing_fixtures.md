## 12: Reviewing Fixtures

* Fixtures are PyTest's mechanism for controlling the "context" around your test cases

* PyTest comes with a number of [built in fixtures](https://docs.pytest.org/en/latest/reference.html#fixtures), though you will likely want to create your own.

* Fixtures are typically functions with the @pytest.fixture decorator:

    * Fixtures can `return` a value, just like a normal function, or `yield` a value like a generator (though only one yield is allowed!), and any post-yield code will be run after the test case has passed or failed.

    * By default, a Fixture will be called (and potentially return or yield a value) once per Test Case it is associated with, though this can be reconfigured in a number of different ways (covered later, though see parameterization below...)

    * (If a fixture raises an unhandled exception, or otherwise fails, the test case won't be run. In the case of a `yield` fixture, this also means that the post-yield code won't be run, either.)

    * Fixtures can be defined "locally", in the same module as the test cases that use them, or "globally" in a `conftest.py` file. (In the event of multiple implementations of a given fixture name, PyTest will prefer the "most local" one, e.g. the fixture located closest to the test case in your file structure.)

* Test cases can have a "dependency" on a fixture:

    * By having a keyword argument whose name matches the fixture

    * (Test cases will fail if their named arguments don't correspond to valid fixtures)

    * Fixtures with parameters (`params`) can cause multiple tests to be created out of a given test case - These "parameterized" tests can pass or fail independently, and are named after the parameters.

    * (It's worth noting that the test instances themselves are the "nodes" in the PyTest testing graph, not the test case functions that you have been writing - This distinction starts to become more apparent with parameters!)

* Fixtures can get "very meta":

    * Fixtures can depend on each other...

    * Fixture dependencies are similar to `import`s, in that even if A depends on B and C, and B depends on C, then C will still only be imported (or in this case, instantiated) once for A.

    * If a test case depends on multiple fixtures that have parameters, the test case will be called with the full cartesian product of all the parameters (e.g. every combination of all the fixture parameters combined).

Fixtures are very complicated, but ultimately very powerful - we've really only scratched the surface here, but hopefully this gives you an overview of what they can do for your tests.

For now, let's move on to another powerful concept...

### Up Next:

[Introduction to Test Marking](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/13_intro_to_test_marking.md)