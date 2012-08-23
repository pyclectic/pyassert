__author__ = "Alexander Metzner"

__all__ = [
    "Matcher",
    "MatcherRegistry",
    "NoSuchMatcherException",
    "register_matcher"
]

class Matcher (object):
    def accepts (self, actual):
        return True

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
        self._matchers = {}
    
    def register_matcher (self, name, matcher_class):
        if name not in self._matchers:
            self._matchers[name] = []
        self._matchers[name].append(matcher_class)
        
    def resolve_matchers (self, name):
        if name not in self._matchers:
            raise NoSuchMatcherException(name)
        return self._matchers[name]


def register_matcher (name):

    def do_register (clazz):
        MatcherRegistry.instance().register_matcher(name, clazz)
        return clazz
    return do_register
