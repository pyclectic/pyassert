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

import sys

from .matcher_registry import Matcher, register_matcher

@register_matcher("raises")
@register_matcher("does_not_raise", negated=True)
class RaisesMatcher(Matcher):
    def __init__(self, expected_exception_type):
        self._expected_exception_type = expected_exception_type
        self._actual_exception_type = None

    def accepts(self, actual):
        return callable(actual)

    def matches(self, actual):
        try:
            actual()
        except:
            self._actual_exception_type = sys.exc_info()[0]
        return self._actual_exception_type == self._expected_exception_type

    def describe(self, actual):
        return "Expected '{0}' to raise exception of type {1} but instead caught {2}".format(actual,
            self._expected_exception_type.__name__, self._actual_exception_type.__name__)

    def describe_negated(self, actual):
        return "Expected '{0}' not to raise exception of type {1}".format(actual,
            self._expected_exception_type.__name__)


