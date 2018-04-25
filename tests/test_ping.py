import unittest

from app import app
 
 
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
 
    # executed after each test
    def tearDown(self):
        pass
 
 
###############
#### tests ####
###############
 
    def test_ping_endpoint(self):
        response = self.app.get('/ping', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"pong")
 
 
if __name__ == "__main__":
    unittest.main()