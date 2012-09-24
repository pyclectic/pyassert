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

class StringMatcher(Matcher):
    "Base class for matchers accepting string values."

    def accepts(self, actual):
        return isinstance(actual, basestring)


class StringMatcherWithArgument(StringMatcher):
    "Base class for matchers accepting string values and requiring additional expected parameter"

    def __init__(self, expected):
        self._expected = expected


@register_matcher("contains")
@register_matcher("does_not_contain", negated=True)
class ContainsMatcher(StringMatcherWithArgument):
    "Tests whether the actual string contains the expected string."

    def matches(self, actual):
        return self._expected in actual

    def describe(self, actual):
        return "Actual '%s' does not contain '%s'" % (actual, self._expected)


@register_matcher("matches")
@register_matcher("does_not_match", negated=True)
class MatchesMatcher(StringMatcherWithArgument):
    "Tests whether the actual string matches the expected regular expression."

    def __init__(self, expected):
        StringMatcherWithArgument.__init__(self, expected)
        self._pattern = re.compile(expected)

    def matches(self, actual):
        return True if self._pattern.match(actual) else False

    def describe(self, actual):
        return "Actual '%s' does not match '%s'" % (actual, self._expected)


@register_matcher("starts_with")
@register_matcher("does_not_start_with", negated=True)
class StartsWithMatcher(StringMatcherWithArgument):
    "Tests whether the actual string starts with the expected string."

    def matches(self, actual):
        return actual.startswith(self._expected)

    def describe(self, actual):
        return "Actual '%s' does not start with '%s'" % (actual, self._expected)


@register_matcher("ends_with")
@register_matcher("does_not_end_with", negated=True)
class EndsWithMatcher(StringMatcherWithArgument):
    "Tests whether the actual string ends with the expected string."

    def matches(self, actual):
        return actual.endswith(self._expected)

    def describe(self, actual):
        return "Actual '%s' does not end with '%s'" % (actual, self._expected)
