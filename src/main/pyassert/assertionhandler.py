__author__ = "Alexander Metzner"

__all__ = [
    "AssertionHandler",
    "assert_that"
]

from .matcher_registry import MatcherRegistry

class AssertionHandler (object):
    def __init__ (self, actual):
        self.actual = actual
        self.matcher_class = None

    def __getattr__ (self, attribute):
        self.matcher_class = MatcherRegistry.instance().resolve_matcher(attribute)
        return self

    def __call__ (self, *arguments, **keywordArguments):
        matcher = self.matcher_class(*arguments, **keywordArguments)
        if not matcher.matches(self.actual):
            raise AssertionError("Assertion failed: %s" % matcher.describe(self.actual))


def assert_that (actual):
    return AssertionHandler(actual)
