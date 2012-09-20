"""
pyassert is a library for rich assertions. All assertions use the central assert_that entry point and can use
built in and custom matchers:

  assert_that('spam').contains('pa').and_ends_with('am')

"""

from .assertionhandler import *
from .matcher_registry import *

from .string_matchers import *
from .object_matchers import *
from .list_matchers import *
from .number_matchers import *

__author__ = "Alexander Metzner, Michael Gruber"

__version__ = "${version}"
