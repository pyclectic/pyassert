import types

from .matcher_registry import Matcher, register_matcher

__author__ = 'Alexander Metzner'

class ListOrTupleMatcher (Matcher):
    def accepts(self, actual):
        return isinstance(actual, types.ListType) or \
            isinstance(actual, types.TupleType)

class AnyOfContainsMatcher (ListOrTupleMatcher):
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
    return AnyOfContainsMatcher(expected_values)


class AllContainsMatcher (ListOrTupleMatcher):
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
    return AllContainsMatcher(expected_values)


@register_matcher("contains")
class ContainsMatcher (ListOrTupleMatcher):
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
