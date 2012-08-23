__author__ = "Alexander Metzner"

__all__ = [
    "AssertionHandler",
    "assert_that"
]

from .matcher_registry import MatcherRegistry

class AssertionHandler (object):
    def __init__ (self, actual):
        self._actual = actual
        self._matcher_name = None
        self._matcher_classes = None

    def __getattr__ (self, attribute):
        self._matcher_name = attribute
        self._matcher_classes = MatcherRegistry.instance().resolve_matchers(attribute)
        return self

    def __call__ (self, *arguments, **keywordArguments):
        for matcher_class in self._matcher_classes:
            matcher = matcher_class(*arguments, **keywordArguments)

            if matcher.accepts(self._actual):
                if not matcher.matches(self._actual):
                    raise AssertionError("Assertion failed: %s" % matcher.describe(self._actual))
                else:
                    return
        raise AssertionError("No matcher named '%s' is able to match actual value '%s' of type '%s'" %
                             (self._matcher_name, self._actual, self._actual.__class__))


def assert_that (actual):
    return AssertionHandler(actual)
