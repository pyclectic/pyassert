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

__author__ = 'Alexander Metzner'

from pyassert.string_matchers import StringMatcher, ContainsMatcher, MatchesMatcher, StartsWithMatcher, EndsWithMatcher

class StringMatcherTests(unittest.TestCase):
    def test_should_accept_string(self):
        self.assertTrue(StringMatcher().accepts('eggs'))

    def test_should_not_accept_list_of_characters(self):
        self.assertFalse(StringMatcher().accepts(['e', 'g', 'g', 's']))


class ContainsMatcherTests(unittest.TestCase):
    def test_should_match_full_string(self):
        self.assertTrue(ContainsMatcher('spam').matches('spam'))

    def test_should_match_partial_string(self):
        self.assertTrue(ContainsMatcher('pa').matches('spam'))

    def test_should_match_prefix_string(self):
        self.assertTrue(ContainsMatcher('spa').matches('spam'))

    def test_should_match_suffix_string(self):
        self.assertTrue(ContainsMatcher('am').matches('spam'))

    def test_should_not_match_no_partial_string(self):
        self.assertFalse(ContainsMatcher('egg').matches('spam'))

    def test_should_match_empty_string(self):
        self.assertTrue(ContainsMatcher('').matches('spam'))

    def test_describe(self):
        self.assertEquals("Actual 'spam' does not contain 'eggs'", ContainsMatcher("eggs").describe("spam"))


class StartsWithMatcherTests(unittest.TestCase):
    def test_should_match_full_string(self):
        self.assertTrue(StartsWithMatcher('spam').matches('spam'))

    def test_should_not_match_partial_string(self):
        self.assertFalse(StartsWithMatcher('pa').matches('spam'))

    def test_should_match_prefix_string(self):
        self.assertTrue(StartsWithMatcher('spa').matches('spam'))

    def test_should_not_match_suffix_string(self):
        self.assertFalse(StartsWithMatcher('am').matches('spam'))

    def test_should_not_match_no_partial_string(self):
        self.assertFalse(StartsWithMatcher('egg').matches('spam'))

    def test_should_match_empty_string(self):
        self.assertTrue(StartsWithMatcher('').matches('spam'))

    def test_describe(self):
        self.assertEquals("Actual 'spam' does not start with 'eggs'", StartsWithMatcher("eggs").describe("spam"))


class EndsWithMatcherTests(unittest.TestCase):
    def test_should_match_full_string(self):
        self.assertTrue(EndsWithMatcher('spam').matches('spam'))

    def test_should_not_match_partial_string(self):
        self.assertFalse(EndsWithMatcher('pa').matches('spam'))

    def test_should_not_match_prefix_string(self):
        self.assertFalse(EndsWithMatcher('spa').matches('spam'))

    def test_should_match_suffix_string(self):
        self.assertTrue(EndsWithMatcher('am').matches('spam'))

    def test_should_not_match_no_partial_string(self):
        self.assertFalse(EndsWithMatcher('egg').matches('spam'))

    def test_should_match_empty_string(self):
        self.assertTrue(EndsWithMatcher('').matches('spam'))

    def test_describe(self):
        self.assertEquals("Actual 'spam' does not end with 'eggs'", EndsWithMatcher("eggs").describe("spam"))


class MatchesMatcherTests(unittest.TestCase):
    def test_should_match_full_string(self):
        self.assertTrue(MatchesMatcher('^spam$').matches('spam'))

    def test_should_match_partial_string(self):
        self.assertTrue(MatchesMatcher('.pa.').matches('spam'))

    def test_should_match_prefix_string(self):
        self.assertTrue(MatchesMatcher('^spa').matches('spam'))

    def test_should_match_suffix_string(self):
        self.assertTrue(MatchesMatcher('.*am$').matches('spam'))

    def test_should_not_match_no_partial_string(self):
        self.assertFalse(MatchesMatcher('egg').matches('spam'))

    def test_should_match_empty_string(self):
        self.assertTrue(MatchesMatcher('').matches('spam'))

    def test_should_match_wildcard_string(self):
        self.assertTrue(MatchesMatcher('.{4}').matches('spam'))

    def test_describe(self):
        self.assertEquals("Actual 'spam' does not match 'eggs'", MatchesMatcher("eggs").describe("spam"))
