import types
import re

from .matcher_registry import Matcher, register_matcher

__author__ = 'Alexander Metzner'

__all__ = [
    "ContainsMatcher"
]

class StringMatcher (Matcher):
    def __init__ (self, expected):
        self._expected = expected

    def accepts(self, actual):
        return isinstance(actual, types.StringType)


@register_matcher("contains")
class ContainsMatcher (StringMatcher):
    def matches (self, actual):
        return self._expected in actual

    def describe (self, actual):
        return "'%s' does not contain '%s'" % (actual, self._expected)


@register_matcher("matches")
class MatchesMatcher (StringMatcher):
    def __init__ (self, expected):
        StringMatcher.__init__(self, expected)
        self._pattern = re.compile(expected)

    def matches (self, actual):
        return True if self._pattern.match(actual) else False

    def describe (self, actual):
        return "'%s' does not match '%s'" % (actual, self._expected)


@register_matcher("starts_with")
class StartsWithMatcher (StringMatcher):
    def matches (self, actual):
        return actual.startswith(self._expected)

    def describe (self, actual):
        return "'%s' does not start with '%s'" % (actual, self._expected)


@register_matcher("ends_with")
class EndsWithMatcher (StringMatcher):
    def matches (self, actual):
        return actual.endswith(self._expected)

    def describe (self, actual):
        return "'%s' does not end with '%s'" % (actual, self._expected)
