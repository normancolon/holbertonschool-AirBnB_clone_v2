#!/usr/bin/python3
"""
Unit tests for the HBNB console.
This script tests the console's functionality and command processing.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand


class ConsoleTest(unittest.TestCase):
    """Defines a test suite for the HBNB console."""

    @classmethod
    def setUpClass(cls):
        """Initial setup for the console test cases."""
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Cleanup resources after all tests have run."""
        del cls.console

    def tearDown(self):
        """Clean up after each test method."""
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            try:
                os.remove("file.json")
            except FileNotFoundError:
                pass

    def test_console_docstrings(self):
        """Test to ensure docstrings are present in the console and its commands."""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_empty_line_execution(self):
        """Test that an empty line input does not execute anything."""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.onecmd("\n")
            self.assertEqual(fake_output.getvalue().strip(), "")


if __name__ == "__main__":
    unittest.main()
