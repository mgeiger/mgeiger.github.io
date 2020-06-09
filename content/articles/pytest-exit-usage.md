title: Pytest Exit Usage
slug: pytest-exit-usage
category: python
date: 2020-06-05 08:20
modified: 2020-06-05
tags: python, pytest, programming
summary: Using the `pytest.exit` method in your code and what to expect for its results.

Most of my information comes from experiences at work. 
I like to document some little tips and tricks I come across while helping my teammates.
Usually I have my methods for getting things accomplished, but I always have a team member who wants something a little unusual when they are writing up their automation tests.

This request was no different.

A coworker has a few tests that they run on a regular basis. 
The initial test they run is an update onto a product. If this test fails, we are in for some major problems and want to stop everything to evaluate the issue.

The caveat is that we only want to stop testing on this single test, not every other test that runs.
The single test that can cause everything to shut down will exit the system prematurely. 
The other tests that will be run can pass, fail, xfail, error, or skip as necessary.

With these little constraints, we had to immediately rule out the `-x` or `--exitfirst` command line option when running `pytest`.
If we run this, we will handle the initial condition that we stop the test when the first one fails, but if we have a failure later on, then we don't finish out the test suite to show if other tests pass and fail.

We started with looking at standard Pytest features that could be used. 
This lead us to the `pytest.exit()` function. 
This function will immediately cause pytest to complete what it is doing, then backout as we are done.
This sounds like something good to work with.

Let's try to make some sample tests that will help us out:
```python
# test_exit.py
import pytest


def test_1():
    assert True


def test_2():
    assert False


def test_3():
    assert False


def test_4():
    assert True
```

Now if we run this file against `pytest` with the following arguments `python -m pytest --verbose --capture=no test_exit.py`, we see the following output:
```
(venv) mgeiger@ThinkPad-X395:~/Projects/trials/python/pytest_exit$ python -m pytest --verbose --capture=no test_exit.py 
======================================= test session starts ========================================
platform linux -- Python 3.8.2, pytest-5.4.3, py-1.8.1, pluggy-0.13.1 -- /home/mgeiger/Projects/trials/python/pytest_exit/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/mgeiger/Projects/trials/python/pytest_exit
collected 4 items                                                                                  

test_exit.py::test_1 PASSED
test_exit.py::test_2 FAILED
test_exit.py::test_3 FAILED
test_exit.py::test_4 PASSED

============================================= FAILURES =============================================
______________________________________________ test_2 ______________________________________________

    def test_2():
>       assert False
E       assert False

test_exit.py:9: AssertionError
______________________________________________ test_3 ______________________________________________

    def test_3():
>       assert False
E       assert False

test_exit.py:13: AssertionError
===================================== short test summary info ======================================
FAILED test_exit.py::test_2 - assert False
FAILED test_exit.py::test_3 - assert False
=================================== 2 failed, 2 passed in 0.12s ====================================

```
