import types

from .matcher_registry import Matcher, register_matcher

__author__ = 'Alexander Metzner'

"""
Provides matcher implementations that deal with lists or tuples.
"""

class ListOrTupleMatcher (Matcher):
    LIST_CLASS = [].__class__
    TUPLE_CLASS = (1,).__class__

    """ Base class for matchers accepting lists or tuples. """
    def accepts(self, actual):
        return actual.__class__ in [ListOrTupleMatcher.LIST_CLASS, ListOrTupleMatcher.TUPLE_CLASS]

class AnyOfContainsMatcher (ListOrTupleMatcher):
    """ 
    Supplementary matcher that matches when any of the expected values
    is contained in the actual collection.
    """ 
    def __init__ (self, expected):
        self.expected = expected

    def matches (self, actual):
        for element in self.expected:
            if element in actual:
                return True
        return False

    def describe (self, actual):
        return "'%s' does not contain any of '%s'" % (actual,
                                                      ", ".join(self.expected))


def any_of (*expected_values):
    """ Convenient factory function for AnyOfContainsMatcher. """
    return AnyOfContainsMatcher(expected_values)


class AllContainsMatcher (ListOrTupleMatcher):
    """ 
    Supplementary matcher that matches when all of the expected values
    are contained in the actual collection.
    """ 
    def __init__ (self, expected):
        self.expected = expected

    def matches (self, actual):
        for element in self.expected:
            if element not in actual:
                return False
        return True

    def describe (self, actual):
        return "'%s' does not contain all elements of '%s'" % (actual,
                                                               ", ".join(self.expected))

def all (*expected_values):
    """ Convenient factory funtion for AllContainsMatcher. """
    return AllContainsMatcher(expected_values)


@register_matcher("contains")
class ContainsMatcher (ListOrTupleMatcher):
    """ 
    Matcher that verifies that certain elements are contained in the given
    collection.
    
    Examples:
    collection = [...]

    assert_that(collection).contains('spam')
    assert_that(collection).contains(any_of('spam', 'eggs'))
    assert_that(collection).contains(all('spam', 'eggs'))
    """
    
    def __init__ (self, expected):
        self.expected = expected

    def matches (self, actual):
        if isinstance(self.expected, Matcher):
            return self.expected.matches(actual)
        return self.expected in actual

    def describe (self, actual):
        if isinstance(self.expected, Matcher):
            return self.expected.describe(actual)
        return "'%s' does not contain '%s'" % (actual, self.expected)
