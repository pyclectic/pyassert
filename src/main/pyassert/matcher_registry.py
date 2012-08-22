__author__ = "Alexander Metzner"

__all__ = [
    "Matcher",
    "MatcherRegistry",
    "NoSuchMatcherException",
    "register_matcher"
]

class Matcher (object):

    def matches (self, actual):
        pass

    def describe (self, actual):
        pass


class NoSuchMatcherException (Exception):
    def __init__ (self, name):
        super(NoSuchMatcherException, self).__init__("No such matcher: %s" % name)


class MatcherRegistry (object):
    _INSTANCE = None
    
    @staticmethod
    def instance ():
        if MatcherRegistry._INSTANCE is None:
            MatcherRegistry._INSTANCE = MatcherRegistry()
        return MatcherRegistry._INSTANCE
    
    def __init__(self):
        self.matchers = {}
    
    def register_matcher (self, name, matcher):
        self.matchers[name] = matcher
        
    def resolve_matcher (self, name):
        if name not in self.matchers:
            raise NoSuchMatcherException(name)
        return self.matchers[name]


def register_matcher (name):

    def do_register (clazz):
        MatcherRegistry.instance().register_matcher(name, clazz)
        return clazz
    return do_register
