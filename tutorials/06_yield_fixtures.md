## 6: Yield Fixtures

Here's a more complicated fixture that uses the `yield` keyword - You may be more accustomed to seeing it used in generator functions, which are typically called repeatedly (e.g. iterated) to deliver their values.

If this seems confusing (or if you aren't familiar with `yield`), don't worry: This is a little different, but the important thing to understand is that `yield` is a lot like `return`, except for one interesting difference...

[tests/05_yield_fixture_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/05_yield_fixture_test.py)

```
pytest -vs tests/05_yield_fixture_test.py
```

Like last time, our fixture ran before the test case that depended on it... Up until the point that we called `yield`. Then our test was run, receiving the "yielded" value as an argument... And then, _after_ the test finished, our fixture picked up where it left off, and ran the rest of the code (after the `yield` call).

This allows us to do both pre-test and post-test actions, with a minimum of code! But there are a few things to keep in mind:

 * Unlike a typical generators, our yield fixtures should never yield more than once. (And PyTest enforces this - try adding a second yield and see what happens: Spoiler Alert! As with many of our hypothetical questions, the result is an unusable test).

    * (If this is messing with your own personal concepts of generators, try not to read too much into it - Fixtures _can_ be generators, and PyTest will use them accordingly, but it expects them to yield exactly once, and that it will perform the first generation before the test case, and the second generation (the "cleanup" code after the `yield`) after the test case completes.

 * There is a corner case to be aware of here: If something goes wrong _inside_ our fixture, such that an unhandled exception is thrown before we call `yield`, we'll never get to the post-yield code... Kind of understandable, if you think about it!
 
    * This may not be the end of the world - it also means we won't actually run the test cases that depend on our broken fixture, so perhaps the post-test cleanup won't be as vital.
    
    * (This doesn't totally kill our test run, either - The tests that depend on the broken fixture will fail during "setup", but PyTest will consider on to other stuff.)
    
    * (If this seems like it might be problematic, depending on what the fixture was trying to do before failed, don't worry:  There are some more thorough cleanup options, which we'll discuss later on.)

### Up Next:

[Request Fixtures](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/07_request_fixtures.md)