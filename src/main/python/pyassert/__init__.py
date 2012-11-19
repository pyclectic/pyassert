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
from .exception_matchers import *
from .filesystem_matchers import *

__author__ = "Alexander Metzner, Michael Gruber"

__version__ = "${version}"
