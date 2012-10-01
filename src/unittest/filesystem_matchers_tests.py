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

__author__ = "Alexander Metzner"

import os
import shutil
import tempfile
import unittest

from pyassert.filesystem_matchers import DirectoryExistsMatcher, FileExistsMatcher, FileLengthMatcher

class TempDirTestBase(unittest.TestCase):
    def setUp(self):
        self.basedir = tempfile.mkdtemp(prefix=self.__class__.__name__)

    def tearDown(self):
        shutil.rmtree(self.basedir)


class DirectoryExistsMatcherTest(TempDirTestBase):
    def test_should_accept_string(self):
        self.assertTrue(DirectoryExistsMatcher().accepts("spam"))

    def test_should_not_accept_non_string(self):
        self.assertFalse(DirectoryExistsMatcher().accepts(None))

    def test_should_match_existing_directory(self):
        dir_name = os.path.join(self.basedir, "spam")
        os.makedirs(dir_name)

        self.assertTrue(DirectoryExistsMatcher().matches(dir_name))

    def test_should_not_match_non_existing_directory(self):
        dir_name = os.path.join(self.basedir, "spam")
        self.assertFalse(DirectoryExistsMatcher().matches(dir_name))

    def test_should_not_match_existing_file(self):
        dir_name = os.path.join(self.basedir, "spam")

        with open(dir_name, "w") as temp_file:
            temp_file.write("")

        self.assertFalse(DirectoryExistsMatcher().matches(dir_name))

    def test_describe(self):
        self.assertEquals("'spam' is not an existing directory", DirectoryExistsMatcher().describe("spam"))

    def test_describe_negated(self):
        self.assertEquals("'spam' is an existing directory", DirectoryExistsMatcher().describe_negated("spam"))


class FileExistsMatcherTest(TempDirTestBase):
    def test_should_accept_string(self):
        self.assertTrue(FileExistsMatcher().accepts("spam"))

    def test_should_not_accept_non_string(self):
        self.assertFalse(FileExistsMatcher().accepts(None))

    def test_should_not_match_existing_directory(self):
        dir_name = os.path.join(self.basedir, "spam")
        os.makedirs(dir_name)

        self.assertFalse(FileExistsMatcher().matches(dir_name))

    def test_should_not_match_non_existing_file(self):
        dir_name = os.path.join(self.basedir, "spam")
        self.assertFalse(FileExistsMatcher().matches(dir_name))

    def test_should_match_existing_file(self):
        dir_name = os.path.join(self.basedir, "spam")

        with open(dir_name, "w") as temp_file:
            temp_file.write("")

        self.assertTrue(FileExistsMatcher().matches(dir_name))

    def test_describe(self):
        self.assertEquals("'spam' is not an existing file", FileExistsMatcher().describe("spam"))

    def test_describe_negated(self):
        self.assertEquals("'spam' is an existing file", FileExistsMatcher().describe_negated("spam"))


class FileLengthMatcherTest(TempDirTestBase):
    def test_should_accept_string(self):
        self.assertTrue(FileLengthMatcher(1).accepts("spam"))

    def test_should_not_accept_non_string(self):
        self.assertFalse(FileLengthMatcher(1).accepts(None))

    def test_should_not_match_existing_directory(self):
        dir_name = os.path.join(self.basedir, "spam")
        os.makedirs(dir_name)

        self.assertFalse(FileLengthMatcher(1).matches(dir_name))

    def test_should_not_match_non_existing_file(self):
        dir_name = os.path.join(self.basedir, "spam")
        self.assertFalse(FileLengthMatcher(1).matches(dir_name))

    def test_should_match_existing_file_with_matching_length(self):
        file_name = os.path.join(self.basedir, "spam")

        with open(file_name, "w") as temp_file:
            temp_file.write("x")

        self.assertTrue(FileLengthMatcher(1).matches(file_name))

    def test_should_match_existing_file_with_matching_length(self):
        file_name = os.path.join(self.basedir, "spam")

        with open(file_name, "w") as temp_file:
            temp_file.write("x")

        self.assertFalse(FileLengthMatcher(2).matches(file_name))

    def test_describe(self):
        self.assertEquals("Actual 'spam' has a length of -1 bytes but expected 1 bytes.",
            FileLengthMatcher(1).describe("spam"))