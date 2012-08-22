from .matcher_registry import Matcher, register_matcher

__author__ = "Alexander Metzner"

@register_matcher("equals")
class EqualsMatcher (Matcher):
    def __init__ (self, expected):
        self.expected = expected

    def matches (self, actual):
        return self.expected == actual 

    def describe (self, actual):
        return "Actual '%s' does not equal expected '%s'" % (actual, 
                                                             self.expected)


class AnyOfContainsMatcher (Matcher):
    def __init__ (self, expected):
        self.expected = expected

    def matches (self, actual):
        for element in self.expected:
            if element in actual:
                return True
        return False

    def describe (self, actual):
        return "'%s' does not contain any of '%s'" % (actual, 
                                                      ", ".join(self.expected))
        

def any_of (*expected_values):
    return AnyOfContainsMatcher(expected_values)


class AllContainsMatcher (Matcher):
    def __init__ (self, expected):
        self.expected = expected

    def matches (self, actual):
        for element in self.expected:
            if element not in actual:
                return False
        return True

    def describe (self, actual):
        return "'%s' does not contain all elements of '%s'" % (actual, 
                                                               ", ".join(self.expected))
        

def all (*expected_values):
    return AllContainsMatcher(expected_values)


@register_matcher("contains")
class ContainsMatcher (Matcher):
    def __init__ (self, expected):
        self.expected = expected
    
    def matches (self, actual):
        if isinstance(self.expected, Matcher):
            return self.expected.matches(actual)
        return self.expected in actual
    
    def describe (self, actual):
        if isinstance(self.expected, Matcher):
            return self.expected.describe(actual)
        return "'%s' does not contain '%s'" % (actual, self.expected)


@register_matcher("is_")
class IsMatcher (Matcher):
    def __init__ (self, expected):
        self.expected = expected
    
    def matches (self, actual):
        return self.expected is actual
    
    def describe (self, actual):
        return "'%s' is not '%s'" % (actual, self.expected)
