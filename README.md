#pyassert [![Build Status](https://secure.travis-ci.org/pyclectic/pyassert.png?branch=master)](https://travis-ci.org/pyclectic/pyassert)

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
* `is_equal_to`/ `equals`/ `is_not_equal_to` - Asserts that two objects are (not) equal (using `==`)
* `is_identical_to`/ `is_not_identical_to` - Asserts that two objects are (not) identical (using `is`)
* `is_none`/ `is_not_none` - Asserts that an object is (not) `None`
* `raises`/ `does_not_raise` - Asserts that a given callable raises/ does not raise an expected exception

#### String Matchers
* `contains`/ `does_not_contain` - Asserts that the actual string contains an expected string
* `ends_with`/ `does_not_end_with` - Asserts that the actual string ends with an expected string
* `is_empty`/ `is_not_empty` - Asserts that the actual string is empty
* `matches`/ `does_not_match` - Asserts that the actual string matches the expected regular expression
* `starts_with`/ `does_not_start_with` - Asserts that actual string starts with the expected string

#### List/ Tuple Matchers
* `contains`/ `does_not_contain` - Asserts that actual list/ tuple contains the expected elements.
* `is_empty`/ `is_not_empty?` - Asserts that actual list/ tuple is empty

#### Boolean Matchers
* `is_true` - Asserts that the actual object is `True`
* `is_false` - Asserts that the actual object is `False`

#### Type Matchers
* `is_instance_of`/ `is_an_instance_of`/ `is_not_an_instance_of` - Asserts that the actual object is an instance of the expected type
* `is_a` - Asserts that the actual object is of the actual type

#### Number Matchers
* `is_less_than`/ `lt` - Asserts that the actual number is less than the expected number
* `is_less_or_equal_than`/ `le` - Asserts that the actual number is less or equal than the expected number
* `is_greater_than`/ `gt` - Asserts that the actual number is greater than the expected number
* `is_greater_or_equal_than`/ `ge` - Asserts that the actual number is greater or equal than the expected number

#### Filesystem Matchers
* `is_a_directory`/ `is_not_a_directory` - Asserts that a given string names an existing directory
* `is_a_file`/ `is_not_a_file` - Asserts that a given string names an existing file
* `has_file_length_of` - Asserts that a given string names an existing file with an expected file length in bytes
* `is_a_empty_file` - Asserts that a given string names an existing empty file
* `is_a_file_with_content` - Asserts that a given string names an existing file with the expected content

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
from pyassert import Matcher, register_matcher

@register_matcher("matches_my_matcher")
class MyMatcher (Matcher):
    ...
```

Now your matcher is available using


```python
assert_that(actual).matches_my_matcher(...)
```

All arguments that are passed to the matches_my_matcher function call are passed to the constructor of MyMatcher that is
used by this assertion.

### Negated Matchers

If you have a matcher that should also be available in a negated manner (such as `contains` and `does_not_contain`) you
can register the matcher twice but set the second one to negated:

```python
from pyassert import Matcher, register_matcher

@register_matcher("matches_my_matcher")
@register_matcher("does_not_match_my_matcher", negated=True)
class MyMatcher (Matcher):
    ...
```

If you also want to provide a custom message that describes the failed, negated state, you can additionally override
the `describe_negated` method in your matcher class. See this example

```python
@register_matcher("is_empty")
@register_negated_matcher("is_not_empty")
class IsEmptyMatcher(ListOrTupleMatcher, StringMatcher):
    def matches(self, actual):
        return len(actual) == 0

    def describe(self, actual):
        return "'%s' is not empty" % actual

    def describe_negated(self, actual):
        return "'%s' is empty" % actual

```

## Release Notes

### Version 0.3.2 released 2013-02-14
* Added `is_a_file_with_content` matcher
* Added `is_a_empty_file` matcher

### Version 0.3.1 released 2012-10-01
* Added `raises`/ `does_not_raise` matcher
* Added filesystem matchers
* Using [six](http://pypi.python.org/pypi/six/) to provide compatibiliy with Python 3

### Version 0.2.5 released 2012-09-24
* Negated matchers

### Version 0.2.4 released 2012-09-20
* Added number matchers
* Added `is_instance_of` matcher
* Added `is_equal_to` as alias to `equals` which is now deprecated
* Hosting project as part of the *pyclectic* organisation

### Version 0.2.3 released 2012-09-11
* Added `is_true` matcher
* Added `is_false` matcher

### Version 0.2.2 released 2012-08-29
* Added `is_none` matcher

### Version 0.2.1 released 2012-08-28
* Added `is_a matcher` that assert that actual values are of an expected type
* pyassert is now compatible with Python 3 (see [Travis Build](http://travis-ci.org/#!/pyclectic/pyassert))
