#!/usr/bin/env python
"""Tests for `Hamming` package."""

import os
import shutil
import unittest

from click.testing import CliRunner

from template import cli
from template.Hamming import hamming


class TestCase(unittest.TestCase):
    """A test class holding example tests using unittest."""

    def setUp(self) -> None:
        """Set up the test case."""

        # List where files and directories to be deleted are marked.
        self._thrashcan = []

        # A constant to be reused in any test function.
        self._constant = "ABCD"

    def tearDown(self) -> None:
        """Clean up after a test has finished."""

        del self._constant

        for item in self._thrashcan:
            if os.path.isfile(item):
                os.remove(item)
            elif os.path.isdir(item):
                shutil.rmtree(item)

    def test_reusing_constant(self):
        """A test that reuses the test class constant"""

        self.assertEqual(self._constant, "ABCD")

    def test_equal(self):
        """Test equality."""

        received = 1
        expected = 1

        self.assertEqual(received, expected)

    def test_lists_equal(self):
        """Test that two lists are equal."""

        received = ["ACTG"]
        expected = ["ACTG"]

        self.assertListEqual(received, expected)

    def test_fails(self):
        """Example for a failing test."""

        received = True

        self.assertTrue(received)

    @unittest.skip("Give me a good reason for skipping!")
    def test_skipped_fails(self):
        """Example for a skipped failing test."""

        received = False

        self.assertTrue(received)

    def test_cli(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)

        self.assertEqual(result.exit_code, 0)
        self.assertIn('python-Hamming-package', result.output)

        help_result = runner.invoke(cli.main, ['--help'])
        self.assertEqual(help_result.exit_code, 0)
        self.assertIn('--help  Show this message and exit.', help_result.output)

    def test_Hamming(self):
        """Test the greeting function."""

        ### absence one sequence
        seq1 = "ATCG"
        seq2 = None
        ham = hamming(seq1, seq2, case = 0)
        expected = None
        self.assertEqual(ham, expected)
        
        ### no string
        seq1 = 23
        seq2 = "ATTA"
        ham = hamming(seq1, seq2, case = 0)
        expected = None
        self.assertEqual(ham, expected)

        ### length
        seq1 = "ACT"
        seq2 = "ATTA"
        ham = hamming(seq1, seq2, case = 0)
        expected = None
        self.assertEqual(ham, expected)

        ### case = 1
        seq1 = "ACTa"
        seq2 = "ATTA"       
        ham = hamming(seq1, seq2, case = 1)
        expected = 1
        self.assertEqual(ham, expected)

        ### ham
        seq1 = "ACTGC"
        seq2 = "ATTAC"
        greet = hamming(seq1, seq2, case = 0)
        expected = 2
        self.assertEqual(ham, expected)


if __name__ == "__main__":
    unittest.main()
