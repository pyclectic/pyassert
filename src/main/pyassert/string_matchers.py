import types
import re

from .matcher_registry import Matcher, register_matcher

__author__ = 'Alexander Metzner'

__all__ = [
    "ContainsMatcher"
]

# Python 3 compatibility
try:
    unicode
except NameError:
    basestring = unicode = str

class StringMatcher (Matcher):
    "Base class for matchers accepting string values."
    def __init__ (self, expected):
        self._expected = expected

    def accepts(self, actual):
        return isinstance(actual, basestring)


@register_matcher("contains")
class ContainsMatcher (StringMatcher):
    "Tests whether the actual string contains the expected string."
    def matches (self, actual):
        return self._expected in actual

    def describe (self, actual):
        return "'%s' does not contain '%s'" % (actual, self._expected)


@register_matcher("matches")
class MatchesMatcher (StringMatcher):
    "Tests whether the actual string matches the expected regular expression."
    def __init__ (self, expected):
        StringMatcher.__init__(self, expected)
        self._pattern = re.compile(expected)

    def matches (self, actual):
        return True if self._pattern.match(actual) else False

    def describe (self, actual):
        return "'%s' does not match '%s'" % (actual, self._expected)


@register_matcher("starts_with")
class StartsWithMatcher (StringMatcher):
    "Tests whether the actual string starts with the expected string."
    def matches (self, actual):
        return actual.startswith(self._expected)

    def describe (self, actual):
        return "'%s' does not start with '%s'" % (actual, self._expected)


@register_matcher("ends_with")
class EndsWithMatcher (StringMatcher):
    "Tests whether the actual string ends with the expected string."
    def matches (self, actual):
        return actual.endswith(self._expected)

    def describe (self, actual):
        return "'%s' does not end with '%s'" % (actual, self._expected)
