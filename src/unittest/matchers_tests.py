import unittest

from pyassert.matchers import EqualsMatcher

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

        