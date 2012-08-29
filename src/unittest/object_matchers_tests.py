import unittest

from pyassert.object_matchers import EqualsMatcher, IsTypeMatcher, IsTrueMatcher, IsFalseMatcher

class EqualsMatcherTest (unittest.TestCase):
    def test_matches_should_return_true_when_values_are_equal (self):
        matcher = EqualsMatcher("spam")
        self.assertTrue(matcher.matches("spam"))

    def test_matches_should_return_false_when_values_are_equal (self):
        matcher = EqualsMatcher("spam")
        self.assertFalse(matcher.matches("eggs"))
        
    def test_describe_should_render_description (self):
        matcher = EqualsMatcher("spam")
        expected = "Actual 'eggs' does not equal expected 'spam'"
        self.assertEquals(expected, matcher.describe("eggs"))


class IsTypeMatcherTest (unittest.TestCase):
    def test_matches_should_return_true_when_value_is_of_expected_class (self):
        class Spam:
            pass
        actual = Spam()
        
        self.assertTrue(IsTypeMatcher(Spam).matches(actual))

    def test_matches_should_return_false_when_value_is_not_of_expected_class (self):
        class Spam:
            pass
        class Egg:
            pass
        actual = Spam()
        
        self.assertFalse(IsTypeMatcher(Egg).matches(actual))

    def test_matches_should_return_true_when_value_is_of_expected_type (self):
        actual = 7
        
        self.assertTrue(IsTypeMatcher(int).matches(actual))

    def test_matches_should_return_false_when_value_is_not_of_expected_type (self):
        actual = 7.7
        
        self.assertFalse(IsTypeMatcher(int).matches(actual))

    def test_describe_should_render_description (self):
        matcher = IsTypeMatcher(int)
        self.assertTrue("eggs" in matcher.describe("eggs"))

class IsTrueMatcherTest (unittest.TestCase):
    def test_should_return_true_when_matching_true (self):
        self.assertTrue(IsTrueMatcher().matches(True))

    def test_should_return_false_when_matching_false (self):
        self.assertFalse(IsTrueMatcher().matches(False))

    def test_should_return_true_when_matching_non_empty_string (self):
        self.assertTrue(IsTrueMatcher().matches("spam"))

    def test_should_return_false_when_matching_non_empty_string (self):
        self.assertFalse(IsTrueMatcher().matches(None))

class IsFalseMatcherTest (unittest.TestCase):
    def test_should_return_false_when_matching_true (self):
        self.assertFalse(IsFalseMatcher().matches(True))

    def test_should_return_true_when_matching_false (self):
        self.assertTrue(IsFalseMatcher().matches(False))

    def test_should_return_false_when_matching_non_empty_string (self):
        self.assertFalse(IsFalseMatcher().matches("spam"))

    def test_should_return_true_when_matching_non_empty_string (self):
        self.assertTrue(IsFalseMatcher().matches(None))
