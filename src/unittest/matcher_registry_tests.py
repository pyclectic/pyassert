
import unittest
from pyassert import MatcherRegistry, Matcher, document_matchers

class MatcherRegistryTest (unittest.TestCase):
    def setUp (self):
        unittest.TestCase.setUp(self)
        self.registry = MatcherRegistry()
    
    def test_should_register_and_resolve_single_matcher (self):
        self.registry.register_matcher("spam", AnyMatcher)
        self.assertEquals([AnyMatcher], self.registry.resolve_matchers("spam"))

    def test_should_register_two_matcher_and_resolve_single_matcher (self):
        self.registry.register_matcher("spam", AnyMatcher)
        self.registry.register_matcher("eggs", AnyOtherMatcher)
        self.assertEquals([AnyMatcher], self.registry.resolve_matchers("spam"))

    def test_should_register_two_matcher_on_the_same_name_and_resolve_two_matcher (self):
        self.registry.register_matcher("spam", AnyMatcher)
        self.registry.register_matcher("spam", AnyOtherMatcher)
        self.assertEquals([AnyMatcher, AnyOtherMatcher], 
                          self.registry.resolve_matchers("spam"))

    def test_should_register_two_matcher_on_the_same_name_list_matcher (self):
        self.registry.register_matcher("spam", AnyMatcher)
        self.registry.register_matcher("spam", AnyOtherMatcher)
        
        actual = self.registry.list_matchers()
        self.assertEquals([("spam", ["any matcher", "any other matcher"])], 
                          actual)

class DocumentMatchersTest (unittest.TestCase):
    def test_document_matchers (self):
        class Writer:
            def write (self, string):
                pass
        document_matchers(Writer())


class AnyMatcher (Matcher):
    """any matcher"""
    pass


class AnyOtherMatcher (Matcher):
    """any other matcher"""
    pass