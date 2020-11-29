import os
import sys
import unittest

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


from app import app, db
 
TEST_DB = 'test.db'
 

class BasicTests(unittest.TestCase):


    def create_app(self):
        return app

    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    # def setUp(self):
    #     app.config['TESTING'] = True
    #     app.config['WTF_CSRF_ENABLED'] = False
    #     app.config['DEBUG'] = False
    #     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    #         os.path.join(SCRIPT_DIR, TEST_DB)
    #     self.app = app()
    #     db.drop_all()
    #     db.create_all()
 
    #     # Disable sending emails during unit testing
    #     # mail.init_app(app)
    #     # self.assertEqual(app.debug, False)
 
    # # executed after each test
    # def tearDown(self):
    #     pass
 
 
###############
#### tests ####
###############
 
    # def test_main_page(self):
    #     response = self.app.get('/pedidos', follow_redirects=True)
    #     self.assertEqual(response.status_code, 200)
 
 
if __name__ == "__main__":
    unittest.main()