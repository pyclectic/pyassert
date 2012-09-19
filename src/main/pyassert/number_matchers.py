__author__ = "Alexander Metzner"

from .matcher_registry import Matcher, register_matcher

class BaseNumberMatcher(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def accepts(self, actual):
        return isinstance(actual, (int, float))


@register_matcher("is_less_than")
class LessThanMatcher(BaseNumberMatcher):
    def describe(self, actual):
        return "Actual '%d' is not less than '%d'" % (actual, self._expected)

    def matches(self, actual):
        return actual < self._expected


class LessThanEqualMatcher(BaseNumberMatcher):
    def describe(self, actual):
        return "Actual '%d' is not less than or equal to '%d'" % (actual, self._expected)

    def matches(self, actual):
        return actual <= self._expected


class GreaterThanMatcher(BaseNumberMatcher):
    def describe(self, actual):
        return "Actual '%d' is not greater than '%d'" % (actual, self._expected)

    def matches(self, actual):
        return actual > self._expected


class GreaterThanEqualMatcher(BaseNumberMatcher):
    def describe(self, actual):
        return "Actual '%d' is not greater than or equal to '%d'" % (actual, self._expected)

    def matches(self, actual):
        return actual >= self._expected
