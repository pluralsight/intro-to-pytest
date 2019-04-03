
## 8: Request "finalizer" Callbacks

Sometimes we want to run a "cleanup" function after testing is complete: We've already covered a very easy way to do this using `yield` [inside a fixture](), but noted that it's not the safest option, if something goes wrong inside our fixture...

Fortunately, PyTest has a `request` plugin (a built-in global fixture) that, among other things, can be used to add a "finalizer", a function which is guaranteed to be called after the fixture (and the test(s) that depend on it) are run... Even in the worst case scenario, where our fixture itself fails, and raises an unhandled exception:

[tests/07_request_finalizer_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/07_request_finalizer_test.py)

```
pytest -vs tests/07_request_finalizer_test.py
```

As usual, we can see that our fixture runs first (including a "risky" function call), followed by our test case, and finally our safe_cleanup function. One advantage of this approach is that we can re-use a shared cleanup function, but the main benefit is that even if our fixture fails to initialize, our finalizer "cleanup" function still gets run!

To really see the finalizer in action, uncomment line 11 in `07_request_finalizer_test.py` (e.g. the commented-out "raise Exception" call), and re-run the test using the command above.

That "risky" function didn't work out - it derailed our fixture, and our test case never even ran! But despite all that, our `safe_cleanup` function still got called.

And in a real test, with a fixture that sets up something complicated or expensive (and might fail _after_ it has made some kind of a mess), guaranteed cleanup could be a really important distinction!

### Up Next:

[Intro to Parameters](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/09_intro_to_parameters.md)