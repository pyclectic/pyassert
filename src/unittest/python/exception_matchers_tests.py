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

import unittest

from pyassert.exception_matchers import RaisesMatcher

class RaisesMatcherTest(unittest.TestCase):
    def test_should_accept_function(self):
        def fun(): pass

        self.assertTrue(RaisesMatcher(BaseException).accepts(fun))

    def test_should_accept_object_with_call_function(self):
        class Callable:
            def __call__(self): pass

        self.assertTrue(RaisesMatcher(BaseException).accepts(Callable()))

    def test_should_not_accept_object_without_call_function(self):
        class NotCallable: pass

        self.assertFalse(RaisesMatcher(BaseException).accepts(NotCallable()))

    def test_should_match_callable_raising_expected_exception(self):
        def closure():
            raise ValueError()

        self.assertTrue(RaisesMatcher(ValueError).matches(closure))

    def test_should_not_match_callable_raising_unexpected_exception(self):
        def closure():
            raise TypeError()

        self.assertFalse(RaisesMatcher(ValueError).matches(closure))

    def test_should_not_match_callable_raising_no_exception(self):
        def closure(): pass

        self.assertFalse(RaisesMatcher(ValueError).matches(closure))

    def test_should_build_description(self):
        matcher = RaisesMatcher(ValueError)
        matcher._actual_exception_type = TypeError
        self.assertEquals("Expected 'spam' to raise exception of type ValueError but instead caught TypeError",
            matcher.describe("spam"))

    def test_should_build_negated_description(self):
        matcher = RaisesMatcher(ValueError)
        self.assertEquals("Expected 'spam' not to raise exception of type ValueError",
            matcher.describe_negated("spam"))
