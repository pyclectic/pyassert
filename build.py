from pythonbuilder.core import init, use_plugin, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.pychecker")
use_plugin("python.distutils")
use_plugin("python.pydev")

default_task = ["analyze", "publish"]

version = "0.2"
summary = "Rich assertions library for Python"
authors = (Author("Alexander Metzner", "halimath.wilanthaou@gmail.com"),)

@init
def init (project):
    project.set_property("dir_source_main_python", "src/main")
    project.set_property("dir_source_unittest_python", "src/unittest")
    project.set_property("distutils_commands", ("sdist", "bdist_dumb"))
    project.set_property("pychecker_break_build", True)
    project.set_property("pychecker_break_build_threshold", 1)
