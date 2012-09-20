from __future__ import print_function

import sys

__author__ = "Alexander Metzner"

__all__ = [
    "Matcher",
    "MatcherRegistry",
    "NoSuchMatcherException",
    "register_matcher",
    "document_matchers"
]

class Matcher(object):
    def accepts(self, actual):
        """Returns True if the given actual value is accepted by this matcher."""
        return True

    def matches(self, actual):
        """Returns True if the given actual value matches this matcher. Returns False otherwise"""
        return False

    def describe(self, actual):
        """Returns a description which is used in case the actual value did not match this matcher's expectation."""
        return "A matcher did not match the actual value."


class NoSuchMatcherException(Exception):
    def __init__(self, name):
        super(NoSuchMatcherException, self).__init__("No such matcher: %s" % name)


class MatcherRegistry(object):
    _INSTANCE = None

    @staticmethod
    def instance():
        if MatcherRegistry._INSTANCE is None:
            MatcherRegistry._INSTANCE = MatcherRegistry()
        return MatcherRegistry._INSTANCE

    def __init__(self):
        self._matchers = {}

    def register_matcher(self, name, matcher_class):
        if name not in self._matchers:
            self._matchers[name] = []
        self._matchers[name].append(matcher_class)

    def resolve_matchers(self, name):
        if name not in self._matchers:
            raise NoSuchMatcherException(name)
        return self._matchers[name]

    def list_matchers(self):
        result = []
        for matcher in self._matchers:
            matcher_doc_strings = []
            for clazz in self._matchers[matcher]:
                matcher_doc_strings.append(clazz.__doc__)
            result.append((matcher, matcher_doc_strings))

        return result


def register_matcher(name):
    def do_register(clazz):
        MatcherRegistry.instance().register_matcher(name, clazz)
        return clazz

    return do_register


def document_matchers(out=sys.stdout):
    matchers = MatcherRegistry.instance().list_matchers()
    result = ""
    for matcher in matchers:
        result += "%s:\n" % matcher[0]
        for doc_string in matcher[1]:
            result += "\t%s\n" % (doc_string if doc_string else "n/a")

    out.write(result)
