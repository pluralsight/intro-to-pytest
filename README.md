# intro-to-pytest
An introduction to PyTest with lots of simple, hackable examples (currently Python 2.7 / 3.6+ compatible).

These examples are intended to be self-explanatory to a Python developer, with minimal setup - In addition to Python 2.7 or 3.6+, you'll also need `pytest` and the `pytest-mock` plugin installed to use all these examples, which you can install by running:

```
pip install -r requirements.txt
```

In this repo (optionally, inside a virtualenv or other environment wrapper, to keep this from affecting your local Python libraries!)

Once you've got all the requirements in place, you should be able to simply run

```
pytest
```

In the repo folder, and see 109 items being collected, and 109 tests passing, in each of the example files, in less than a second.

(PyTest will list the names of each test module file that it found, and then a period for each test case that passed, or other symbols for tests that failed, were skipped, etc.)

But if you're seeing all that, congratulations! You're ready to get started.

The recommended approach is to read each example file, then run it directly with pytest, with the `v` flag (so that each Test Case is listed by name) and the `s` flag, so that we can see the raw output from the Tests, which will help explain how each example is working; PyTest normally captures and hides this output, except for tests that are failing. (In the examples below, we'll shorten these arguements to `-vs`.)

Each example test was intended to be self-explanatory, but I have begun adding short tutorial guides to explain more of the context, suggest experiments and hacks you can attempt on th examples, and to provide recaps and reviews for each major section. The tutorial track starts with:

[Tutorial Zero: An Empty Test](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/00_empty_test.md)

Not all of the examples have an accompanying tutorial (yet), but were written to be self-explanatory, and should at least include basic comments to explain the feature being demonstrated.

If you have any feedback, questions, or PyTest features you'd like to see covered, please let me know on Pluralsight Slack as [@david.sturgis](https://pluralsight.slack.com/team/U036DTQQ1), or via email at [david-sturgis@pluralsight.com](mailto:david-sturgis@pluralsight.com), or via [GitHub Issues](https://github.com/pluralsight/intro-to-pytest/issues) (or a PR, now that I have PR notifcations turned on!).
