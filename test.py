import unittest
from app import app
from selenium import webdriver

class BTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_bucketviews(self):
        tester = app.test_client(self)
        response = tester.get('/viewblist.html', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_bucketviews(self):
        tester = app.test_client(self)
        response = tester.get('/login.html', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_bucketviews(self):
        tester = app.test_client(self)
        response = tester.get('/register.html', content_type='html/text')
        self.assertEqual(response.status_code, 200)

class bucketlistTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()#It opens the browser
        self.browser.implicitly_wait(3)#waitss for 3 seconds if it needs to

    def tearDown(self):		#runs after each test. It closes the browser.
        self.browser.quit()

    def test_body(self):		#asserts that the title of the webpage has Home in it.
        self.browser.get('http://127.0.0.1:5000/')
        self.assertIn('Home', self.browser.title)

    def test_body(self):		#asserts that the title of the webpage has Home in it.
        self.browser.get('http://127.0.0.1:5000/')
        self.assertIn('Create the bucketlist below', self.browser.body)

if __name__ == '__main__':
    unittest.main()
