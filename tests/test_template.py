#!/usr/bin/env python
"""Tests for `template` package."""

import unittest
import os
import sys
import shutil
import pytest
from click.testing import CliRunner

from template import cli
from template.template import greeting


class TestCase(unittest.TestCase):
    """ A test class holding example tests using unittest. """

    def setUp(self) -> None:
        """ Set up the test case. """

        # List where files and directories to be deleted are marked.
        self._thrashcan = []

        # A constant to be reused in any test function.
        self._constant = "ABCD"

    def tearDown(self) -> None:
        """ Clean up after a test has finished."""

        del self._constant

        for item in self._thrashcan:
            if os.path.isfile(item):
                os.remove(item)
            elif os.path.isdir(item):
                shutil.rmtree(item)

    def test_reusing_constant(self):
        """ A test that reuses the test class constant"""

        self.assertEqual(self._constant, "ABCD")

    def test_equal(self):
        """Test equality."""

        received = 1
        expected = 1

        self.assertEqual(received, expected)

    def test_lists_equal(self):
        """ Test that two lists are equal."""

        received = ["ACTG"]
        expected = ["ACTG"]

        self.assertListEqual(received, expected)

    def test_fails(self):
        """ Example for a failing test."""

        received = False

        self.assertTrue(received)

    @unittest.skip("Give me a good reason for skipping!")
    def test_skipped_fails(self):
        """ Example for a skipped failing test."""

        received = False

        self.assertTrue(received)

    def test_cli(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)

        self.assertEqual(result.exit_code, 0)
        self.assertIn('python-template-package', result.output)

        help_result = runner.invoke(cli.main, ['--help'])
        self.assertEqual(help_result.exit_code, 0)
        self.assertIn('--help  Show this message and exit.', help_result.output)

    def test_greeting(self):
        """ Test the greeting function."""

        mood = "sad"

        greet = greeting(mood)
        expected = "How are you? I'm sad."

        self.assertEqual(greet, expected)

        ### TODO: Add other moods.

if __name__ == "__main__":
    unittest.main()
