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

import random
import unittest
from mockito import mock, when, verify, any as any_value

from pyassert import MatcherRegistry, Matcher, NegatedMatcherDecorator, register_matcher

class MatcherTest(unittest.TestCase):
    def setUp(self):
        self.matcher = Matcher()

    def test_should_accept_everything(self):
        self.assertTrue(self.matcher.accepts(None))

    def test_should_match_nothing(self):
        self.assertFalse(self.matcher.matches(None))

    def test_describe(self):
        self.assertEquals("A matcher did not match the actual value.", self.matcher.describe(None))


class MatcherRegistryTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.registry = MatcherRegistry()

    def test_should_register_and_resolve_single_matcher(self):
        self.registry.register_matcher("spam", AnyMatcher)
        self.assertEquals([AnyMatcher], self.registry.resolve_matchers("spam"))

    def test_should_register_two_matcher_and_resolve_single_matcher(self):
        self.registry.register_matcher("spam", AnyMatcher)
        self.registry.register_matcher("eggs", AnyOtherMatcher)
        self.assertEquals([AnyMatcher], self.registry.resolve_matchers("spam"))

    def test_should_register_two_matcher_on_the_same_name_and_resolve_two_matcher(self):
        self.registry.register_matcher("spam", AnyMatcher)
        self.registry.register_matcher("spam", AnyOtherMatcher)
        self.assertEquals([AnyMatcher, AnyOtherMatcher],
            self.registry.resolve_matchers("spam"))


class NegatedMatcherDecoratorTest(unittest.TestCase):
    def test_should_delegate_accept_calls(self):
        actual_mock = mock()

        matcher_mock = mock(Matcher)
        when(matcher_mock).accepts(any_value()).thenReturn(True)

        matcher = NegatedMatcherDecorator(matcher_mock)

        self.assertTrue(matcher.accepts(actual_mock))

        verify(matcher_mock).accepts(actual_mock)

    def test_should_delegate_and_invert_matches_calls(self):
        actual_mock = mock()

        matcher_mock = mock(Matcher)
        when(matcher_mock).matches(any_value()).thenReturn(True)

        matcher = NegatedMatcherDecorator(matcher_mock)

        self.assertFalse(matcher.matches(actual_mock))

        verify(matcher_mock).matches(actual_mock)

    def test_should_invoke_describe_negated_when_describe_is_called(self):
        actual_mock = mock()

        matcher_mock = mock(Matcher)
        when(matcher_mock).describe_negated(any_value()).thenReturn("spam")

        matcher = NegatedMatcherDecorator(matcher_mock)

        self.assertEquals("spam", matcher.describe(actual_mock))

        verify(matcher_mock).describe_negated(actual_mock)
        verify(matcher_mock, 0).describe(actual_mock)


class MatcherRegistrationIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(5))

    def test_should_register_matcher(self):
        @register_matcher(self.name)
        class SomeMatcher(Matcher): pass

        self.assertEquals([SomeMatcher], MatcherRegistry.instance().resolve_matchers(self.name))

    def test_should_register_negated_matcher(self):
        @register_matcher(self.name, negated=True)
        class SomeMatcher(Matcher): pass

        matcher = MatcherRegistry.instance().resolve_matchers(self.name)[0]()

        self.assertTrue(isinstance(matcher, NegatedMatcherDecorator))


class AnyMatcher(Matcher):
    """any matcher"""


class AnyOtherMatcher(Matcher):
    """any other matcher"""