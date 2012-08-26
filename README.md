
#pyassert [![Build Status](https://secure.travis-ci.org/halimath/pyassert.png?branch=master)](http://travis-ci.org/halimath/pyassert)

pyassert is an assertion library for the Python programming language. 

##Introduction

Assertions are used in automated tests to verify that a given piece of code behaves as expected. pyassert aims to provide assertions with provide

* **rich functionality**: common assertions should be expressed easily
* **good readability**: assertions should be easy to read and easy to understand to enhance the overall understandability of the test
* **independent of the test framework**: pyassert assertions work with every Python test environment.

## How to install it?

pyassert is available via the [Cheeseshop](http://pypi.python.org/pypi/pyassert/) so you can use easy_install or pip:

    $ pip install pyassert

## How to use it?

The most important function pyassert provides is **assert_that**. This function is used to start an assertion. You pass
in the actual value and as a result you get an AssertionHandler (although you will never care, most of the time).

The AssertionHandler provides several assertion predicates. These are functions you can use to verify a given state
of the actual value.

Some examples:

```python
from pyassert import *

assert_that('spam and eggs').ends_with('eggs')
assert_that(['spam', 'and', 'eggs']).contains(any_of('spam', 'ham'))
```

The general structure is

   assert_that(actual_value).matcher_name(expected_values)

Every assertion will return None if the actual value matches the expectations or raise an AssertionError with a
readable message in case the expectations are not met.

###Matchers

The following matcher are provided by pyassert.

#### Common Matchers
* equals
* is_identical_to

#### String Matchers
* contains
* matches
* ends_with
* starts_with

#### List/ Tuple Matchers
* contains

## How to extend it?

pyassert uses Matchers to match actual values against expected values. A matcher is simply a
class extending the pyassert Matcher class which looks like this:

```python
class Matcher (object):
    def accepts (self, actual):
        """Returns True if the given actual value is accepted by this matcher."""
        return True

    def matches (self, actual):
        """Returns True if the given actual value matches this matcher. Returns False otherwise"""
        pass

    def describe (self, actual):
        """Returns a description which is used in case the actual value did not match this matcher's expectation."""
        pass
```

Once you have created your Matcher you need to register it. The registration is done with
a class decorator register_matcher providing the name of the matcher


```python

@register_matcher("matches_my_matcher")
class MyMatcher (matcher):
    ...
```

Now your matcher is available using


```python
assert_that(actual).matches_my_matcher(...)
```

All arguments that are passed to the matches_my_matcher function call are passed to the constructor of MyMatcher that is used by this assertion.
