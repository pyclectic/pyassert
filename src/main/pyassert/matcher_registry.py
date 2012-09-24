from __future__ import print_function

import sys

__author__ = "Alexander Metzner"

__all__ = [
    "Matcher",
    "NegatedMatcherDecorator",
    "MatcherRegistry",
    "NoSuchMatcherException",
    "register_matcher",
    "register_negated_matcher"
]

class Matcher(object):
    """
    Interface class for matcher objects. Matcher objects are used to accept and match expected with actual values
    and in case of a difference to provide a description on the mismatch.
    """

    def accepts(self, actual):
        """Returns True if the given actual value is accepted by this matcher."""
        return True

    def matches(self, actual):
        """Returns True if the given actual value matches this matcher. Returns False otherwise"""
        return False

    def describe(self, actual):
        """Returns a description which is used in case the actual value did not match this matcher's expectation."""
        return "A matcher did not match the actual value."

    def describe_negated(self, actual):
        """
        Used to provide a negated description when the matcher is used in a negated context.
        """
        return "NOT: %s" % self.describe(actual)


class NegatedMatcherDecorator(Matcher):
    """
    Decorator used to decorate a given matcher for use in a negated context.
    """

    def __init__(self, target_matcher):
        self._target_matcher = target_matcher

    def accepts(self, actual):
        return self._target_matcher.accepts(actual)


    def matches(self, actual):
        return not self._target_matcher.matches(actual)

    def describe(self, actual):
        return self._target_matcher.describe_negated(actual)


class NoSuchMatcherException(Exception):
    "to be thrown when no matcher with a given name was found"

    def __init__(self, name):
        super(NoSuchMatcherException, self).__init__("No such matcher: %s" % name)


class MatcherRegistry(object):
    """
    Registry of all available matchers.

    The registry is a singleton class which is used to register a matcher factory for a given name and later retrieve
    that matcher when assertions are made.

    The interaction with the singleton instance is wrapped using the register_matcher decorator and the
    AssertionHandler.
    """
    _INSTANCE = None

    @staticmethod
    def instance():
        "Singleton retrieval method"
        if MatcherRegistry._INSTANCE is None:
            MatcherRegistry._INSTANCE = MatcherRegistry()
        return MatcherRegistry._INSTANCE

    def __init__(self):
        self._matchers = {}

    def register_matcher(self, name, matcher_factory):
        "Registers the given matcher_factory (class or function) for the given name"
        if name not in self._matchers:
            self._matchers[name] = []
        self._matchers[name].append(matcher_factory)

    def resolve_matchers(self, name):
        """
        Returns all matcher factories registered for the given name.
        Throws a NoSuchMatcherException when no matchers are found.
        """
        if name not in self._matchers:
            raise NoSuchMatcherException(name)
        return self._matchers[name]


def register_matcher(name, negated=False):
    """
    Decorator used to register a class or a factory method as a matcher.

    The optional argument `negated` defines whether the matcher instances operate as normal matchers or negated which
    means that the result of a matching operation will be inverted (negated).

    Example given

      @register_matcher("is_no_spam")
      class IsNoSpamMatcher (Matcher):
          ...
    """
    def do_register(clazz):
        if negated:
            def factory(*arguments, **keyword_arguments):
                matcher = clazz(*arguments, **keyword_arguments)
                return NegatedMatcherDecorator(matcher)

            MatcherRegistry.instance().register_matcher(name, factory)
        else:
            MatcherRegistry.instance().register_matcher(name, clazz)
        return clazz

    return do_register


def register_negated_matcher(name):
    """
    Convenience function used to decorate negated matchers:

      @register_negated_matcher(name)

    is equal to

      @register_matcher(name, negated=True)
    """
    return register_matcher(name, negated=True)
