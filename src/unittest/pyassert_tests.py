import unittest

from pyassert import *

class IntegrationTest (unittest.TestCase):
    def test_assert_that_should_raise_exception_when_no_matcher_with_method_name_is_found (self):
        def callback ():
            assert_that("spam").matcher_not_found("spam")
        self.assertRaises(NoSuchMatcherException, callback)
    
    def test_that_equal_matcher_matches_equal_values (self):
        assert_that("spam").equals("spam")

    def test_that_equal_matcher_does_not_match_inequal_values (self):
        try:
            assert_that("spam").equals("eggs")
            self.fail("AssertionError expected")
        except AssertionError as e:
            self.assertEquals("Assertion failed: Actual 'spam' does not equal expected 'eggs'", str(e))

    def test_that_contains_matcher_matches_value_that_contains_expected (self):
        assert_that("spam").contains("pa")

    def test_that_contains_matcher_does_not_match_value_that_does_not_contain_expected (self):
        try:
            assert_that("spam").contains("eggs")
            self.fail("AssertionError expected")
        except AssertionError as e:
            self.assertEquals("Assertion failed: 'spam' does not contain 'eggs'", str(e))
            
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
        
    def test_that_is_matches_identical_object (self):
        assert_that(True).is_(True)

    def test_that_is_does_not_match_no_identical_object (self):
        self.assertRaises(AssertionError, assert_that(True).is_, False)

    def test_that_not_negates_match (self):
        assert_that(False).is_(not True)
