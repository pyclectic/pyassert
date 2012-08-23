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


@register_matcher("is_")
class IsMatcher (Matcher):
    def __init__ (self, expected):
        self.expected = expected

    def matches (self, actual):
        return self.expected is actual

    def describe (self, actual):
        return "'%s' is not '%s'" % (actual, self.expected)

