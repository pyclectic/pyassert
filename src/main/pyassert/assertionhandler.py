__author__ = "Alexander Metzner"

__all__ = [
    "AssertionHandler",
    "assert_that",
    "InvalidUsageException"
]

from .matcher_registry import MatcherRegistry

class InvalidUsageException(Exception):
    def __init__(self, name):
        self._message = "Must not use 'and_' as first matcher: '%s'" % name

    def __str__(self):
        return self._message


class AssertionHandler(object):
    def __init__(self, actual):
        self._actual = actual
        self._matcher_name = None
        self._matcher_classes = None
        self._matches = 0

    def __getattr__(self, attribute):
        self._matcher_name = self._filter_matcher_name(attribute)
        self._matcher_classes = MatcherRegistry.instance().resolve_matchers(self._matcher_name)
        return self

    def __call__(self, *arguments, **keywordArguments):
        for matcher_class in self._matcher_classes:
            matcher = matcher_class(*arguments, **keywordArguments)

            if matcher.accepts(self._actual):
                if not matcher.matches(self._actual):
                    raise AssertionError("Assertion failed: %s" % matcher.describe(self._actual))
                else:
                    self._matches += 1
                    return self
        raise AssertionError("No matcher named '%s' is able to match actual value '%s' of type '%s'" %
                             (self._matcher_name, self._actual, self._actual.__class__))

    def _filter_matcher_name(self, name):
        if name.startswith("and_"):
            if self._matches == 0:
                raise InvalidUsageException(name)
            return name[4:]
        return name


def assert_that(actual):
    return AssertionHandler(actual)
