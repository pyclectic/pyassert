__author__ = "Alexander Metzner"

import unittest

from pyassert.list_matchers import IsEmptyMatcher, IsNotEmptyMatcher, AnyOfContainsMatcher, AllContainsMatcher


class AnyOfContainsMatcherTest(unittest.TestCase):
    def test_matches_should_return_true_when_element_matches(self):
        self.assertTrue(AnyOfContainsMatcher(["spam", "eggs"]).matches(["spam"]))

    def test_matches_should_return_false_when_not_element_matches(self):
        self.assertFalse(AnyOfContainsMatcher(["spam", "eggs"]).matches(["foo"]))

    def test_describe(self):
        self.assertEquals("Actual '['spam']' does not contain any of 'foo, bar'",
            AnyOfContainsMatcher(["foo", "bar"]).describe(["spam"]))


class AllContainsMatcherTest(unittest.TestCase):
    def test_matches_should_return_true_when_element_matches_all_elements(self):
        self.assertTrue(AllContainsMatcher(["spam", "eggs"]).matches(["spam", "eggs"]))

    def test_matches_should_return_false_when_no_element_matches(self):
        self.assertFalse(AllContainsMatcher(["spam", "eggs"]).matches(["foo"]))

    def test_matches_should_return_false_when_only_some_element_match(self):
        self.assertFalse(AllContainsMatcher(["spam", "eggs"]).matches(["spam"]))

    def test_describe(self):
        self.assertEquals("Actual '['spam']' does not contain all elements of 'foo, bar'",
            AllContainsMatcher(["foo", "bar"]).describe(["spam"]))


class IsEmptyMatcherTest(unittest.TestCase):
    def test_should_match_empty_list(self):
        self.assertTrue(IsEmptyMatcher().matches([]))

    def test_should_match_empty_tuple(self):
        empty_tuple = tuple()

        self.assertTrue(IsEmptyMatcher().matches(empty_tuple))

    def test_should_not_match_non_empty_list(self):
        self.assertFalse(IsEmptyMatcher().matches(['spam']))

    def test_should_match_empty_tuple(self):
        self.assertFalse(IsEmptyMatcher().matches(('spam',)))

    def test_describe(self):
        self.assertEquals("'['spam']' is not empty", IsEmptyMatcher().describe(['spam']))


class IsNotEmptyMatcherTest(unittest.TestCase):
    def test_should_not_match_empty_list(self):
        self.assertFalse(IsNotEmptyMatcher().matches([]))

    def test_should_not_match_empty_tuple(self):
        empty_tuple = tuple()

        self.assertFalse(IsNotEmptyMatcher().matches(empty_tuple))

    def test_should_match_non_empty_list(self):
        self.assertTrue(IsNotEmptyMatcher().matches(['spam']))

    def test_should_empty_tuple(self):
        self.assertTrue(IsNotEmptyMatcher().matches(('spam',)))

    def test_describe(self):
        self.assertEquals("'[]' is empty", IsNotEmptyMatcher().describe([]))
