import unittest
import os
import sqlite3
from application import app, init_db, DB_PATH

class FlaskAppUnitTests(unittest.TestCase):

    def setUp(self):
        """Set up test client and initialize test database"""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()
        # Use a test database
        global DB_PATH
        import application
        application.DB_PATH = 'test_database.db'
        init_db()

    def tearDown(self):
        """Remove test database after each test"""
        if os.path.exists('test_database.db'):
            os.remove('test_database.db')

    def test_home_page_loads(self):
        """Test that home page loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_form(self):
        """Test that home page contains the message form"""
        response = self.client.get('/')
        self.assertIn(b'name', response.data)

    def test_add_message(self):
        """Test adding a new message"""
        response = self.client.post('/add', data={
            'name': 'Test User',
            'message': 'Hello World'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_add_message_appears_on_page(self):
        """Test that added message appears on home page"""
        self.client.post('/add', data={
            'name': 'Laiba',
            'message': 'Test Message'
        }, follow_redirects=True)
        response = self.client.get('/')
        self.assertIn(b'Laiba', response.data)

    def test_add_empty_message_ignored(self):
        """Test that empty name/message is ignored"""
        response = self.client.post('/add', data={
            'name': '',
            'message': ''
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_database_initialized(self):
        """Test that database and table are created"""
        conn = sqlite3.connect('test_database.db')
        cursor = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='messages'"
        )
        result = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(result)

    def test_multiple_messages(self):
        """Test adding multiple messages"""
        self.client.post('/add', data={'name': 'User1', 'message': 'Msg1'}, follow_redirects=True)
        self.client.post('/add', data={'name': 'User2', 'message': 'Msg2'}, follow_redirects=True)
        response = self.client.get('/')
        self.assertIn(b'User1', response.data)
        self.assertIn(b'User2', response.data)

    def test_redirect_after_add(self):
        """Test that /add redirects to home page"""
        response = self.client.post('/add', data={
            'name': 'Test',
            'message': 'Message'
        })
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
