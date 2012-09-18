import unittest

from pyassert import *

class BasicAcceptanceTest (unittest.TestCase):
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

    def test_should_chain_matcher (self):
        assert_that("spam and eggs").contains("and").and_ends_with("eggs")

    def test_should_not_allow_and_matcher_as_first_matcher (self):
        def callback ():
            assert_that("spam and eggs").and_contains("and")
        self.assertRaises(InvalidUsageException, callback)


class ObjectMatchersAcceptanceTest (unittest.TestCase):
    def test_that_equal_matcher_matches_equal_values (self):
        assert_that("spam").equals("spam")

    def test_that_equal_matcher_does_not_match_inequal_values (self):
        try:
            assert_that("spam").equals("eggs")
            self.fail("AssertionError expected")
        except AssertionError as e:
            self.assertEquals("Assertion failed: Actual 'spam' does not equal expected 'eggs'", str(e))

    def test_that_is_equal_to_matcher_matches_equal_values (self):
        assert_that("spam").is_equal_to("spam")

    def test_that_is_equal_to_matcher_does_not_match_inequal_values (self):
        try:
            assert_that("spam").is_equal_to("eggs")
            self.fail("AssertionError expected")
        except AssertionError as e:
            self.assertEquals("Assertion failed: Actual 'spam' does not equal expected 'eggs'", str(e))

    def test_that_is_identical_to_matches_identical_object (self):
        assert_that(True).is_identical_to(True)

    def test_that_is_identical_to_does_not_match_no_identical_object (self):
        try:
            assert_that(True).is_identical_to(False)
            self.fail("AssertionError expected")
        except (AssertionError) as e:
            pass

    def test_that_not_negates_match (self):
        assert_that(False).is_identical_to(not True)
        
    def test_is_of_type (self):
        assert_that(7).is_a(int)

    def test_is_true (self):
        assert_that(4).is_true()

    def test_is_false (self):
        assert_that(None).is_false()

    def test_is_none (self):
        assert_that(None).is_none()


class StringMatchersAcceptanceTest (unittest.TestCase):
    def test_contains (self):
        assert_that("spam").contains("pa")

    def test_contains_fail (self):
        try:
            assert_that("spam").contains("egg")
            self.fail("AssertionError expected")
        except (AssertionError) as e:
            pass

    def test_matches (self):
        assert_that("spam").matches(".*pa.*")

    def test_matches_fail (self):
        try:
            assert_that("spam").matches("egg")
            self.fail("AssertionError expected")
        except (AssertionError) as e:
            pass

    def test_starts_with (self):
        assert_that("spam").starts_with("sp")

    def test_starts_with_fail (self):
        try:
            assert_that("spam").starts_with("egg")
            self.fail("AssertionError expected")
        except (AssertionError) as e:
            pass

    def test_ends_with (self):
        assert_that("spam").ends_with("am")

    def test_ends_with_fail (self):
        try:
            assert_that("spam").ends_with("egg")
            self.fail("AssertionError expected")
        except (AssertionError) as e:
            pass

    def test_that_is_empty_matcher_matches_empty_string (self):
        assert_that('').is_empty()

    def test_that_is_empty_matcher_does_not_match_non_empty_string (self):
        try:
            assert_that('spam').is_empty()
            self.fail("AssertionError expected")
        except (AssertionError) as e:
            pass


    def test_that_is_not_empty_matcher_matches_non_empty_string (self):
        assert_that('spam').is_not_empty()

    def test_that_is_not_empty_matcher_does_not_match_empty_string (self):
        try:
            assert_that('').is_not_empty()
            self.fail("AssertionError expected")
        except (AssertionError) as e:
            pass

class ListMatchersAcceptanceTest (unittest.TestCase):
    def test_that_contains_matcher_matches_single_element_in_list (self):
        assert_that(["a", "b", "c"]).contains("a")

    def test_that_contains_matcher_does_not_match_single_element_not_in_list (self):
        try:
            assert_that(["a", "b", "c"]).contains("d")
            self.fail("AssertionError expected")
        except (AssertionError) as e:
            pass

    def test_that_contains_matcher_matches_when_any_of_is_used_and_one_element_matches (self):
        assert_that(["a", "b", "c"]).contains(any_of("a", "d"))

    def test_that_contains_matcher_does_not_match_when_any_of_is_used_and_no_element_matches (self):
        try:
            assert_that(["a", "b", "c"]).contains(any_of("d", "e"))
            self.fail("AssertionError expected")
        except (AssertionError) as e:
            pass

    def test_that_contains_matcher_does_not_match_when_all_is_used_and_not_all_elements_match (self):
        try:
            assert_that(["a", "b", "c"]).contains(all("a", "d"))
            self.fail("AssertionError expected")
        except (AssertionError) as e:
            pass

    def test_that_contains_matcher_matches_when_all_is_used_and_all_elements_match (self):
        assert_that(["a", "b", "c"]).contains(all("a", "b"))

    def test_that_is_empty_matcher_matches_empty_list (self):
        assert_that([]).is_empty()

    def test_that_is_empty_matcher_does_not_match_non_empty_list (self):
        try:
            assert_that(['spam']).is_empty()
            self.fail("AssertionError expected")
        except (AssertionError) as e:
            pass

    def test_that_is_not_empty_matcher_matches_non_empty_list (self):
        assert_that(['spam']).is_not_empty()

    def test_that_is_not_empty_matcher_does_not_match_empty_list (self):
        try:
            assert_that([]).is_not_empty()
            self.fail("AssertionError expected")
        except (AssertionError) as e:
            pass


class IsInstanceOfTest (unittest.TestCase):
    def test_success (self):
        assert_that([1, 2, 3]).is_instance_of(list)

    def test_failure (self):
        try:
            assert_that([1, 2, 3]).is_instance_of(dict)
            self.fail("AssertionError expected")
        except AssertionError as e:
            pass