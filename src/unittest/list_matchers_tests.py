
import unittest

from pyassert.list_matchers import IsEmptyMatcher, IsNotEmptyMatcher

__author__ = 'Alexander Metzner'

class IsEmptyMatcherTest (unittest.TestCase):
    def test_should_match_empty_list (self):
        self.assertTrue(IsEmptyMatcher().matches([]))

    def test_should_match_empty_tuple (self):
        empty_tuple = tuple()

        self.assertTrue(IsEmptyMatcher().matches(empty_tuple))

    def test_should_not_match_non_empty_list (self):
        self.assertFalse(IsEmptyMatcher().matches(['spam']))

    def test_should_match_empty_tuple (self):
        self.assertFalse(IsEmptyMatcher().matches(('spam',)))

    def test_describe (self):
        self.assertEquals("'['spam']' is not empty", IsEmptyMatcher().describe(['spam']))

class IsNotEmptyMatcherTest (unittest.TestCase):
    def test_should_not_match_empty_list (self):
        self.assertFalse(IsNotEmptyMatcher().matches([]))

    def test_should_not_match_empty_tuple (self):
        empty_tuple = tuple()

        self.assertFalse(IsNotEmptyMatcher().matches(empty_tuple))

    def test_should_match_non_empty_list (self):
        self.assertTrue(IsNotEmptyMatcher().matches(['spam']))

    def test_should_empty_tuple (self):
        self.assertTrue(IsNotEmptyMatcher().matches(('spam',)))

    def test_describe (self):
        self.assertEquals("'[]' is empty", IsNotEmptyMatcher().describe([]))
