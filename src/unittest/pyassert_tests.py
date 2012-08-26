import unittest

from pyassert import *

class BasicIntegrationTest (unittest.TestCase):
    def test_assert_that_should_raise_exception_when_no_matcher_with_method_name_is_found (self):
        def callback ():
            assert_that("spam").matcher_not_found("spam")
        self.assertRaises(NoSuchMatcherException, callback)

    def test_assert_that_should_raise_exception_when_no_matcher_accepts_the_actual_value (self):
        class AnyObject:
            pass
        def callback ():
            assert_that(AnyObject()).contains("something")
        self.assertRaises(AssertionError, callback)


class ObjectMatchersIntegrationTest (unittest.TestCase):
    def test_that_equal_matcher_matches_equal_values (self):
        assert_that("spam").equals("spam")

    def test_that_equal_matcher_does_not_match_inequal_values (self):
        try:
            assert_that("spam").equals("eggs")
            self.fail("AssertionError expected")
        except AssertionError as e:
            self.assertEquals("Assertion failed: Actual 'spam' does not equal expected 'eggs'", str(e))

    def test_that_is_identical_to_matches_identical_object (self):
        assert_that(True).is_identical_to(True)

    def test_that_is_identical_to_does_not_match_no_identical_object (self):
        self.assertRaises(AssertionError, assert_that(True).is_identical_to, False)

    def test_that_not_negates_match (self):
        assert_that(False).is_identical_to(not True)
        
    def test_is_of_type (self):
        assert_that(7).is_a(int)


class StringMatchersIntegrationTest (unittest.TestCase):
    def test_contains (self):
        assert_that("spam").contains("pa")

    def test_contains_fail (self):
        self.assertRaises(AssertionError, assert_that("spam").contains, "egg")

    def test_matches (self):
        assert_that("spam").matches(".*pa.*")

    def test_matches_fail (self):
        self.assertRaises(AssertionError, assert_that("spam").matches, "egg")

    def test_starts_with (self):
        assert_that("spam").starts_with("sp")

    def test_starts_with_fail (self):
        self.assertRaises(AssertionError, assert_that("spam").starts_with, "egg")

    def test_ends_with (self):
        assert_that("spam").ends_with("am")

    def test_ends_with_fail (self):
        self.assertRaises(AssertionError, assert_that("spam").ends_with, "egg")


class ListMatchersIntegrationTest (unittest.TestCase):
    def test_that_contains_matcher_matches_single_element_in_list (self):
        assert_that(["a", "b", "c"]).contains("a")

    def test_that_contains_matcher_does_not_match_single_element_not_in_list (self):
        self.assertRaises(AssertionError, assert_that(["a", "b", "c"]).contains, "d")

    def test_that_contains_matcher_matches_when_any_of_is_used_and_one_element_matches (self):
        assert_that(["a", "b", "c"]).contains(any_of("a", "d"))

    def test_that_contains_matcher_does_not_match_when_any_of_is_used_and_no_element_matches (self):
        self.assertRaises(AssertionError, assert_that(["a", "b", "c"]).contains, any_of("d", "e"))

    def test_that_contains_matcher_does_not_match_when_all_is_used_and_not_all_elements_match (self):
        self.assertRaises(AssertionError, assert_that(["a", "b", "c"]).contains, all("a", "d"))

    def test_that_contains_matcher_matches_when_all_is_used_and_all_elements_match (self):
        assert_that(["a", "b", "c"]).contains(all("a", "b"))
