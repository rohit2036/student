import unittest
from app import create_app, db
from app.models import Student

class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app.config['TESTING'] = True
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_student(self):
        response = self.client.post('/api/v1/students', json={
            'name': 'John Doe', 'age': 20, 'grade': 'A'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_all_students(self):
        self.client.post('/api/v1/students', json={'name': 'Test', 'age': 21, 'grade': 'B'})
        response = self.client.get('/api/v1/students')
        self.assertEqual(response.status_code, 200)

    def test_healthcheck(self):
        response = self.client.get('/healthcheck')
        self.assertEqual(response.status_code, 200)
