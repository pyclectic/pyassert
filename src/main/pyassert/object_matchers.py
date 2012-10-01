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

from .matcher_registry import Matcher, register_matcher

__author__ = "Alexander Metzner"

class BaseMatcher(Matcher):
    "Base class for matchers that have a single expected value."

    def __init__(self, expected):
        self._expected = expected


@register_matcher("equals")
@register_matcher("is_equal_to")
@register_matcher("is_not_equal_to", negated=True)
class EqualsMatcher(BaseMatcher):
    "Matcher that tests whether two object are equal, i.e. actual == expected"

    def matches(self, actual):
        return self._expected == actual

    def describe(self, actual):
        return "Actual '%s' does not equal expected '%s'" % (actual,
                                                             self._expected)


@register_matcher("is_identical_to")
@register_matcher("is_not_identical_to", negated=True)
class IsMatcher(BaseMatcher):
    "Matcher that tests whether two objects are identical, i.e. actual is expected"

    def matches(self, actual):
        return self._expected is actual

    def describe(self, actual):
        return "Actual '%s' is not '%s'" % (actual, self._expected)


@register_matcher("is_a")
class IsTypeMatcher(BaseMatcher):
    """
    Matcher that tests whether the actual value is of a given type.
    
    Examples
    
    assert_that(7).is_a(int)
    assert_that(7.2).is_a(float)
    """

    def matches(self, actual):
        return self._expected is actual.__class__

    def describe(self, actual):
        return "'%s' of type %s is not of expected type %s" % (actual,
                                                               actual.__class__,
                                                               self._expected)


@register_matcher("is_true")
class IsTrueMatcher(Matcher):
    def matches(self, actual):
        return bool(actual)

    def describe(self, actual):
        return "Actual '%s' is not True" % actual


@register_matcher("is_false")
class IsFalseMatcher(Matcher):
    def matches(self, actual):
        return not bool(actual)

    def describe(self, actual):
        return "Actual '%s' is not False" % actual


@register_matcher("is_none")
@register_matcher("is_not_none", negated=True)
class NoneMatcher(Matcher):
    def matches(self, actual):
        return actual is None

    def describe(self, actual):
        return "Actual '%s' is not None" % actual


@register_matcher("is_instance_of")
@register_matcher("is_an_instance_of")
@register_matcher("is_not_an_instance_of", negated=True)
class InstanceOfMatcher(BaseMatcher):
    def matches(self, actual):
        return isinstance(actual, self._expected)

    def describe(self, actual):
        return "Actual '%s' is not an instance of %s" % (actual, self._expected.__name__)


