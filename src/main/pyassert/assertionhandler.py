#  pyassert
#  Copyright 2012 The pyassert team.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

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
        for matcher_factory in self._matcher_classes:
            matcher = matcher_factory(*arguments, **keywordArguments)

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
            if not self._matches:
                raise InvalidUsageException(name)
            return name[4:]
        return name


def assert_that(actual):
    return AssertionHandler(actual)
