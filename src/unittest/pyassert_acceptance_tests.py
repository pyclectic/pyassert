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

import unittest

from pyassert import *

class FrameworkAcceptanceTest(unittest.TestCase):
    def test_assert_that_should_raise_exception_when_no_matcher_with_method_name_is_found(self):
        def callback():
            assert_that("spam").matcher_not_found("spam")

        self.assertRaises(NoSuchMatcherException, callback)

    def test_assert_that_should_raise_exception_when_no_matcher_accepts_the_actual_value(self):
        class AnyObject:
            pass

        def callback():
            assert_that(AnyObject()).contains("something")

        self.assertRaises(AssertionError, callback)

    def test_should_chain_matcher(self):
        assert_that("spam and eggs").contains("and").and_ends_with("eggs")

    def test_should_not_allow_and_matcher_as_first_matcher(self):
        def callback():
            assert_that("spam and eggs").and_contains("and")

        self.assertRaises(InvalidUsageException, callback)


class MatcherAccepanceTest(unittest.TestCase):
    def test_equals(self):
        assert_that("spam").equals("spam")

    def test_is_equal_to(self):
        assert_that("spam").is_equal_to("spam")

    def test_is_not_equal_to(self):
        assert_that("spam").is_not_equal_to("eggs")

    def test_is_identical_to(self):
        assert_that(True).is_identical_to(True)

    def test_is_not_identical_to(self):
        assert_that(True).is_not_identical_to(False)

    def test_is_of_type(self):
        assert_that(7).is_a(int)

    def test_is_true(self):
        assert_that(4).is_true()

    def test_is_false(self):
        assert_that(None).is_false()

    def test_is_none(self):
        assert_that(None).is_none()

    def test_is_not_none(self):
        assert_that("spam").is_not_none()

    def test_string_contains(self):
        assert_that("spam").contains("pa")

    def test_string_does_not_contain(self):
        assert_that("spam").does_not_contain("eggs")

    def test_matches(self):
        assert_that("spam").matches(".*pa.*")

    def test_does_not_match(self):
        assert_that("spam").does_not_match(".*e.*")

    def test_string_starts_with(self):
        assert_that("spam").starts_with("sp")

    def test_does_not_start_with(self):
        assert_that("spam").does_not_start_with("eggs")

    def test_does_not_end_with(self):
        assert_that("spam").does_not_end_with("egg")

    def test_string_is_empty(self):
        assert_that('').is_empty()

    def test_string_is_not_empty(self):
        assert_that('spam').is_not_empty()

    def test_list_that_contains(self):
        assert_that(["a", "b", "c"]).contains("a")

    def test_list_contains_any_of(self):
        assert_that(["a", "b", "c"]).contains(any_of("a", "d"))

    def test_list_contains_all(self):
        assert_that(["a", "b", "c"]).contains(all("a", "b"))

    def test_list_is_not_empty(self):
        assert_that(['spam']).is_not_empty()

    def test_is_instance_of(self):
        assert_that([1, 2, 3]).is_instance_of(list)

    def test_is_an_instance_of(self):
        assert_that([1, 2, 3]).is_an_instance_of(list)

    def test_is_not_an_instance_of(self):
        assert_that([1, 2, 3]).is_not_an_instance_of(tuple)

    def test_is_less_than(self):
        assert_that(1).is_less_than(2)

    def test_is_less_or_equal_than(self):
        assert_that(1).is_less_or_equal_than(1)

    def test_is_greater_than(self):
        assert_that(2).is_greater_than(1)

    def test_is_greater_or_equal_than(self):
        assert_that(1).is_greater_or_equal_than(1)

    def test_lt(self):
        assert_that(1).lt(2)

    def test_le(self):
        assert_that(1).le(1)

    def test_gt(self):
        assert_that(2).gt(1)

    def test_ge(self):
        assert_that(1).ge(1)

    def test_raises (self):
        def closure():
            raise ValueError()

        assert_that(closure).raises(ValueError)

    def test_does_not_raise (self):
        def closure():
            raise TypeError()

        assert_that(closure).does_not_raise(ValueError)
