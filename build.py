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
pyassert is an assertion library for the Python programming language.

Introduction
------------

Assertions are used in automated tests to verify that a given piece of code behaves as expected. pyassert aims to provide assertions with provide

* **rich functionality**: common assertions should be expressed easily
* **good readability**: assertions should be easy to read and easy to understand to enhance the overall understandability of the test
* **independent of the test framework**: pyassert assertions work with every Python test environment.

How to install it?
``````````````````

pyassert is available via the [Cheeseshop](http://pypi.python.org/pypi/pyassert/) so you can use easy_install or pip:

    $ pip install pyassert


Links
`````

* pyassert Github repository including documentation <https://github.com/pyclectic/pyassert>
"""

from pybuilder.core import init, use_plugin, Author

use_plugin("filter_resources")

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.pychecker")
use_plugin("python.distutils")

use_plugin("python.install_dependencies")
use_plugin("python.pydev")

default_task = ["analyze", "publish"]

version = "0.4.1"
summary = "Rich assertions library for Python"
description = __doc__
authors = (Author("Alexander Metzner", "halimath.wilanthaou@gmail.com"),
           Author("Michael Gruber", "aelgru@gmail.com"))
url = "https://github.com/pyclectic/pyassert"
license = "Apache Software License"

@init
def init (project):
    project.depends_on("six")

    project.build_depends_on("coverage")
    project.build_depends_on("mockito")

    project.get_property("filter_resources_glob").append("**/pyassert/__init__.py")

    project.set_property("pychecker_break_build", False)
    project.set_property("pychecker_break_build_threshold", 1)
    
    project.set_property("coverage_threshold_warn", 90)
    project.set_property("coverage_break_build", True)

    project.get_property("distutils_commands").append("bdist_egg")
    project.set_property("distutils_classifiers", [
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing"])
