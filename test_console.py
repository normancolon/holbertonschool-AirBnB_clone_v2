#!/usr/bin/python3
"""
A unit test module for the console (command interpreter).
"""
import sys
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.user import User
from models.base_model import BaseModel
from models import storage
from console import HBNBCommand
import MySQLdb
import os
import unittest
from io import StringIO
from unittest.mock import patch
import pycodestyle
sys.path.append('/home/lol/holbertonschool-AirBnB_clone_v2')


class TestFileStorageConsole(unittest.TestCase):
    """
    Tests for FileStorage related console functionality.
    """

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     'Skipping FileStorage tests')
    def test_fs_create_persistence(self):
        """
        Test object creation and persistence with FileStorage.
        """
        with patch('sys.stdout', new_callable=StringIO) as cout:
            HBNBCommand().onecmd('create City name="San Francisco"')
            city_id = cout.getvalue().strip()
            self.assertTrue(city_id)
            HBNBCommand().onecmd('save')
            storage.reload()
            self.assertIn('City.{}'.format(city_id), storage.all())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     'Skipping FileStorage tests')
    def test_fs_save_reload_object(self):
        """
        Test saving and reloading an object with FileStorage.
        """
        with patch('sys.stdout', new_callable=StringIO) as cout:
            HBNBCommand().onecmd('create BaseModel name="Test Reload"')
            obj_id = cout.getvalue().strip()
        self.assertTrue(obj_id)
        HBNBCommand().onecmd('save')
        storage.reload()
        self.assertIn('BaseModel.{}'.format(obj_id), storage.all())
        self.assertEqual(storage.all()['BaseModel.{}'.format(obj_id)].name,
                         "Test Reload")


class TestDBStorageConsole(unittest.TestCase):
    """Tests for DBStorage related console functionality."""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "DBStorage tests only")
    def test_db_create(self):
        """Tests create command with database storage, checks user creation."""
        cmd = 'create User email="john25@gmail.com" password="123"'
        with patch('sys.stdout', new_callable=StringIO) as cout:
            HBNBCommand().onecmd(cmd)
            user_id = cout.getvalue().strip()
            self.verify_user_creation_in_db(user_id)

    # Include other DBStorage test methods here...


class TestCreateCommand(unittest.TestCase):
    """
    Test cases for creating objects via the HBNB console command 'create'.
    """

    def setUp(self):
        """Set up test case."""
        self.consol = HBNBCommand()

    def test_create_state_simple(self):
        """Test creating a State with no additional parameters."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.consol.onecmd("create State")
            state_id = mock_stdout.getvalue().strip()
            self.assertIsNotNone(state_id)
            self.assertTrue(len(state_id) > 0)

    def test_create_state_with_name(self):
        """Test creating a State with a name parameter."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.consol.onecmd("create State name=\"California\"")
            state_id = mock_stdout.getvalue().strip()
            self.assertIsNotNone(state_id)
            self.assertTrue(len(state_id) > 0)
            state_obj = storage.all()["State.{}".format(state_id)]
            self.assertEqual(state_obj.name, "California")

    # Additional methods to test other scenarios...

    def tearDown(self):
        """Clean up resources after tests."""


class TestConsoleDocs(unittest.TestCase):
    """
    Tests to assess the documentation and coding style of the console app.
    """

    def test_pycodestyle_conformance_console(self):
        """
        Test that console.py conforms to PEP8/pycodestyle.
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "console.py does not follow PEP8 guidelines.")

    def test_pycodestyle_conformance_test_console(self):
        """
        Test that console tests conform to PEP8/pycodestyle.
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "tests/test_console.py does not follow PEP8.")

    def test_console_module_docstring_exists(self):
        """Check for existence of console.py module docstring."""
        module = sys.modules[HBNBCommand.__module__]
        self.assertIsNotNone(
            module.__doc__, "console.py module lacks a docstring.")

    def test_HBNBCommand_class_docstring_exists(self):
        """
        Check for existence of the HBNBCommand class docstring.
        """
        self.assertIsNotNone(HBNBCommand.__doc__,
                             "HBNBCommand class lacks a docstring.")


class TestHBNBCommand(unittest.TestCase):
    """
    Represents the test class for the HBNBCommand class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up resources before any tests are run.
        """
        cls.consol = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """
        Clean up resources after all tests have run.
        """
        del cls.consol

    def setUp(self):
        """
        Set up the test environment before each test.
        """
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        """
        Clean up after each test.
        """
        sys.stdout = self.held

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     'Skipping FileStorage tests')
    def test_fs_create(self):
        """
        Tests the create command with the file storage.
        """
        with patch('sys.stdout', new_callable=StringIO) as cout:
            HBNBCommand().onecmd('create City name="Texas"')
            mdl_id = cout.getvalue().strip()
            self.assertIn('City.{}'.format(mdl_id), storage.all())
            HBNBCommand().onecmd('show City {}'.format(mdl_id))
            self.assertIn('name="Texas"', cout.getvalue())

# Below are the added DBStorage tests


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
def test_db_create(self):
    """Tests create command with database storage, checks user creation."""
    cmd = 'create User email="john25@gmail.com" password="123"'
    with patch('sys.stdout', new_callable=StringIO) as cout:
        HBNBCommand().onecmd(cmd)
        user_id = cout.getvalue().strip()
        self.verify_user_creation_in_db(user_id)


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
def test_db_show(self):
    """Tests the show command for an object in database storage."""
    # Implementation similar to test_db_create, verifying object retrieval


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
def test_db_destroy(self):
    """Tests destroy command for an object in database storage."""
    # Test logic here to ensure object deletion is reflected in the database


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
def test_db_all(self):
    """Tests the all command with DBStorage."""
    # Test to verify 'all' command functionality with DBStorage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
def test_db_update(self):
    """Tests the update command with DBStorage."""
    # Test to verify 'update' command functionality with DBStorage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
def test_db_count(self):
    """Tests the count command with the database storage."""
    initial_count = storage.count('State')
    HBNBCommand().onecmd('create State name="Lagos"')
    final_count = storage.count('State')
    self.assertEqual(final_count, initial_count + 1)


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
def test_fs_destroy(self):
    """Test object destruction with FileStorage."""
    cmd = 'create User name="Test User"'
    with patch('sys.stdout', new_callable=StringIO) as cout:
        HBNBCommand().onecmd(cmd)
        user_id = cout.getvalue().strip()
        self.ensure_user_deletion(user_id)


def verify_user_creation_in_db(self, user_id):
    """Helper function to verify user creation in database."""
    db_conn = MySQLdb.connect(host=os.getenv('HBNB_MYSQL_HOST'),
                              user=os.getenv('HBNB_MYSQL_USER'),
                              passwd=os.getenv('HBNB_MYSQL_PWD'),
                              db=os.getenv('HBNB_MYSQL_DB'))
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    self.assertTrue(result[0] > 0, "User not created in database")
    cursor.close()
    db_conn.close()


def ensure_user_deletion(self, user_id):
    HBNBCommand().onecmd('create User name="Test User"')
    user_id = cout.getvalue().strip()

    # Ensure the User object was created
    self.assertTrue(user_id)
    self.assertIn(f'User.{user_id}', storage.all().keys())

    # Destroy the created User object
    HBNBCommand().onecmd(f'destroy User {user_id}')

    # Ensure the User object is no longer present
    self.assertNotIn(f'User.{user_id}', storage.all().keys())


if __name__ == "__main__":
    unittest.main()
