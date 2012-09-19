__author__ = "Alexander Metzner"

import unittest

from pyassert.number_matchers import BaseNumberMatcher, LessThanMatcher, LessThanEqualMatcher, GreaterThanMatcher,\
    GreaterThanEqualMatcher

class BaseNumberMatcherTest(unittest.TestCase):
    def setUp(self):
        self.matcher = BaseNumberMatcher(87)

    def test_should_accept_integer(self):
        self.assertTrue(self.matcher.accepts(int(7)))

    def test_should_accept_float(self):
        self.assertTrue(self.matcher.accepts(float(2.3)))

    def test_should_not_accept_string(self):
        self.assertFalse(self.matcher.accepts(str(2)))


class LessThanMatcherTest(unittest.TestCase):
    def setUp(self):
        self.matcher = LessThanMatcher(7)

    def test_should_return_true_when_matching_value_less_than_expected(self):
        self.assertTrue(self.matcher.matches(6))

    def test_should_return_false_when_matching_value_equal_than_expected(self):
        self.assertFalse(self.matcher.matches(7))

    def test_should_return_false_when_matching_value_greater_than_expected(self):
        self.assertFalse(self.matcher.matches(8))

    def test_should_provide_description(self):
        self.assertEquals("Actual '7' is not less than '7'", self.matcher.describe(7))


class LessThanEqualMatcherTest(unittest.TestCase):
    def setUp(self):
        self.matcher = LessThanEqualMatcher(7)

    def test_should_return_true_when_matching_value_less_than_expected(self):
        self.assertTrue(self.matcher.matches(6))

    def test_should_return_true_when_matching_value_equal_than_expected(self):
        self.assertTrue(self.matcher.matches(7))

    def test_should_return_false_when_matching_value_greater_than_expected(self):
        self.assertFalse(self.matcher.matches(8))

    def test_should_provide_description(self):
        self.assertEquals("Actual '8' is not less than or equal to '7'", self.matcher.describe(8))


class GreaterThanMatcherTest(unittest.TestCase):
    def setUp(self):
        self.matcher = GreaterThanMatcher(7)

    def test_should_return_false_when_matching_value_less_than_expected(self):
        self.assertFalse(self.matcher.matches(6))

    def test_should_return_false_when_matching_value_equal_than_expected(self):
        self.assertFalse(self.matcher.matches(7))

    def test_should_return_true_when_matching_value_greater_than_expected(self):
        self.assertTrue(self.matcher.matches(8))

    def test_should_provide_description(self):
        self.assertEquals("Actual '7' is not greater than '7'", self.matcher.describe(7))


class GreaterThanEqualMatcherTest(unittest.TestCase):
    def setUp(self):
        self.matcher = GreaterThanEqualMatcher(7)

    def test_should_return_false_when_matching_value_less_than_expected(self):
        self.assertFalse(self.matcher.matches(6))

    def test_should_return_true_when_matching_value_equal_than_expected(self):
        self.assertTrue(self.matcher.matches(7))

    def test_should_return_true_when_matching_value_greater_than_expected(self):
        self.assertTrue(self.matcher.matches(8))

    def test_should_provide_description(self):
        self.assertEquals("Actual '6' is not greater than or equal to '7'", self.matcher.describe(6))
