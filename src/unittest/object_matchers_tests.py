import unittest

from pyassert.object_matchers import EqualsMatcher, IsTypeMatcher, IsTrueMatcher, IsFalseMatcher, NoneMatcher,\
    InstanceOfMatcher, IsMatcher

class IsMatcherTest(unittest.TestCase):
    def test_matches_should_return_true_when_objects_are_identical(self):
        first = []
        second = first

        self.assertTrue(IsMatcher(first).matches(second))

    def test_matches_should_return_false_when_objects_are_not_identical(self):
        first = []
        second = []

        self.assertFalse(IsMatcher(first).matches(second))

    def test_describe(self):
        self.assertEquals("Actual '[]' is not '[]'", IsMatcher([]).describe([]))


class EqualsMatcherTest(unittest.TestCase):
    def test_matches_should_return_true_when_values_are_equal(self):
        matcher = EqualsMatcher("spam")
        self.assertTrue(matcher.matches("spam"))

    def test_matches_should_return_false_when_values_are_equal(self):
        matcher = EqualsMatcher("spam")
        self.assertFalse(matcher.matches("eggs"))

    def test_describe_should_render_description(self):
        matcher = EqualsMatcher("spam")
        expected = "Actual 'eggs' does not equal expected 'spam'"
        self.assertEquals(expected, matcher.describe("eggs"))


class IsTypeMatcherTest(unittest.TestCase):
    def test_matches_should_return_true_when_value_is_of_expected_class(self):
        class Spam:
            pass

        actual = Spam()

        self.assertTrue(IsTypeMatcher(Spam).matches(actual))

    def test_matches_should_return_false_when_value_is_not_of_expected_class(self):
        class Spam:
            pass

        class Egg:
            pass

        actual = Spam()

        self.assertFalse(IsTypeMatcher(Egg).matches(actual))

    def test_matches_should_return_true_when_value_is_of_expected_type(self):
        actual = 7

        self.assertTrue(IsTypeMatcher(int).matches(actual))

    def test_matches_should_return_false_when_value_is_not_of_expected_type(self):
        actual = 7.7

        self.assertFalse(IsTypeMatcher(int).matches(actual))

    def test_describe_should_render_description(self):
        matcher = IsTypeMatcher(int)
        self.assertTrue("eggs" in matcher.describe("eggs"))


class IsTrueMatcherTest(unittest.TestCase):
    def test_should_return_true_when_matching_true(self):
        self.assertTrue(IsTrueMatcher().matches(True))

    def test_should_return_false_when_matching_false(self):
        self.assertFalse(IsTrueMatcher().matches(False))

    def test_should_return_true_when_matching_non_empty_string(self):
        self.assertTrue(IsTrueMatcher().matches("spam"))

    def test_should_return_false_when_matching_non_empty_string(self):
        self.assertFalse(IsTrueMatcher().matches(None))

    def test_describe(self):
        self.assertEquals("Actual '[]' is not True", IsTrueMatcher().describe([]))


class IsFalseMatcherTest(unittest.TestCase):
    def test_should_return_false_when_matching_true(self):
        self.assertFalse(IsFalseMatcher().matches(True))

    def test_should_return_true_when_matching_false(self):
        self.assertTrue(IsFalseMatcher().matches(False))

    def test_should_return_false_when_matching_non_empty_string(self):
        self.assertFalse(IsFalseMatcher().matches("spam"))

    def test_should_return_true_when_matching_non_empty_string(self):
        self.assertTrue(IsFalseMatcher().matches(None))

    def test_describe(self):
        self.assertEquals("Actual '[]' is not False", IsFalseMatcher().describe([]))


class IsNoneMatcherTest(unittest.TestCase):
    def test_should_return_true_when_matching_None(self):
        self.assertTrue(NoneMatcher().matches(None))

    def test_should_return_false_when_matching_string(self):
        self.assertFalse(NoneMatcher().matches(""))

    def test_describe(self):
        self.assertEquals("Actual '[]' is not None", NoneMatcher().describe([]))


class InstanceOfMatcherTest(unittest.TestCase):
    def test_should_match_value_when_class_matches(self):
        self.assertTrue(InstanceOfMatcher(list).matches([1, 2, 3]))

    def test_should_not_match_value_when_class_does_not_match(self):
        self.assertFalse(InstanceOfMatcher(list).matches("asd"))

    def test_should_build_description(self):
        self.assertEquals(InstanceOfMatcher(list).describe("spam"), "Actual 'spam' is not an instance of list")