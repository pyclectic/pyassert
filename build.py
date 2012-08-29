from pythonbuilder.core import init, use_plugin, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.pychecker")
use_plugin("python.distutils")

use_plugin("python.install_dependencies")
use_plugin("python.pydev")

default_task = ["analyze", "publish"]

version = "0.2.2"
summary = "Rich assertions library for Python"
description = """
pyassert is an assertion library for the Python programming language. pyassert aims to provide assertions with provide

* rich functionality: common assertions should be expressed easily
* good readability: assertions should be easy to read and easy to understand to enhance the overall understandability of the test
* independent of the test framework: pyassert assertions work with every Python test environment.
"""
authors = (Author("Alexander Metzner", "halimath.wilanthaou@gmail.com"),)
url = "https://github.com/halimath/pyassert"
license = "Apache Software License"

@init
def init (project):
    project.build_depends_on("coverage")

    project.set_property("dir_source_main_python", "src/main")
    project.set_property("dir_source_unittest_python", "src/unittest")
    project.set_property("pychecker_break_build", True)
    project.set_property("pychecker_break_build_threshold", 1)
    
    project.set_property("coverage_threshold_warn", 90)
    project.set_property("coverage_break_build", True)

    project.get_property("distutils_commands").append("bdist_egg")
    project.set_property("distutils_classifiers", [
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing'])
