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

from .matcher_registry import Matcher, register_matcher

class BaseNumberMatcher(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def accepts(self, actual):
        return isinstance(actual, (int, float))


@register_matcher("is_less_than")
@register_matcher("lt")
class LessThanMatcher(BaseNumberMatcher):
    def describe(self, actual):
        return "Actual '%d' is not less than '%d'" % (actual, self._expected)

    def matches(self, actual):
        return actual < self._expected


@register_matcher("is_less_or_equal_than")
@register_matcher("le")
class LessThanEqualMatcher(BaseNumberMatcher):
    def describe(self, actual):
        return "Actual '%d' is not less than or equal to '%d'" % (actual, self._expected)

    def matches(self, actual):
        return actual <= self._expected


@register_matcher("is_greater_than")
@register_matcher("gt")
class GreaterThanMatcher(BaseNumberMatcher):
    def describe(self, actual):
        return "Actual '%d' is not greater than '%d'" % (actual, self._expected)

    def matches(self, actual):
        return actual > self._expected


@register_matcher("is_greater_or_equal_than")
@register_matcher("ge")
class GreaterThanEqualMatcher(BaseNumberMatcher):
    def describe(self, actual):
        return "Actual '%d' is not greater than or equal to '%d'" % (actual, self._expected)

    def matches(self, actual):
        return actual >= self._expected
