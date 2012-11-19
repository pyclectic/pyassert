#  pyassert
#  Copyright 2012 The pyassert team.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""
Provides matcher implementations that deal with lists or tuples.
"""

__author__ = 'Alexander Metzner'

from .string_matchers import StringMatcher
from .matcher_registry import Matcher, register_matcher, register_negated_matcher


class ListOrTupleMatcher(Matcher):
    """ Base class for matchers accepting lists or tuples. """
    LIST_CLASS = [].__class__
    TUPLE_CLASS = (1,).__class__


    def accepts(self, actual):
        return actual.__class__ in [ListOrTupleMatcher.LIST_CLASS, ListOrTupleMatcher.TUPLE_CLASS]


class AnyOfContainsMatcher(ListOrTupleMatcher):
    """ 
    Supplementary matcher that matches when any of the expected values
    is contained in the actual collection.
    """

    def __init__(self, expected):
        self.expected = expected

    def matches(self, actual):
        for element in self.expected:
            if element in actual:
                return True
        return False

    def describe(self, actual):
        return "Actual '%s' does not contain any of '%s'" % (actual,
                                                             ", ".join(self.expected))


def any_of(*expected_values):
    """ Convenient factory function for AnyOfContainsMatcher. """
    return AnyOfContainsMatcher(expected_values)


class AllContainsMatcher(ListOrTupleMatcher):
    """ 
    Supplementary matcher that matches when all of the expected values
    are contained in the actual collection.
    """

    def __init__(self, expected):
        self.expected = expected

    def matches(self, actual):
        for element in self.expected:
            if element not in actual:
                return False
        return True

    def describe(self, actual):
        return "Actual '%s' does not contain all elements of '%s'" % (actual,
                                                                      ", ".join(self.expected))


def all(*expected_values):
    """ Convenient factory funtion for AllContainsMatcher. """
    return AllContainsMatcher(expected_values)


@register_matcher("contains")
class ContainsMatcher(ListOrTupleMatcher):
    """ 
    Matcher that verifies that certain elements are contained in the given
    collection.
    
    Examples:
    collection = [...]

    assert_that(collection).contains('spam')
    assert_that(collection).contains(any_of('spam', 'eggs'))
    assert_that(collection).contains(all('spam', 'eggs'))
    """

    def __init__(self, expected):
        self.expected = expected

    def matches(self, actual):
        if isinstance(self.expected, Matcher):
            return self.expected.matches(actual)
        return self.expected in actual

    def describe(self, actual):
        if isinstance(self.expected, Matcher):
            return self.expected.describe(actual)
        return "'%s' does not contain '%s'" % (actual, self.expected)


@register_matcher("is_empty")
@register_negated_matcher("is_not_empty")
class IsEmptyMatcher(ListOrTupleMatcher, StringMatcher):
    def accepts(self, actual):
        return ListOrTupleMatcher.accepts(self, actual) or StringMatcher.accepts(self, actual)

    def matches(self, actual):
        return len(actual) == 0

    def describe(self, actual):
        return "'%s' is not empty" % actual

    def describe_negated(self, actual):
        return "'%s' is empty" % actual
