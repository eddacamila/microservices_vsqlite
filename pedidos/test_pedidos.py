import os
import sys
import unittest
import flask_testing

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


from app import app, db
 
TEST_DB = 'test.db'
 

class BasicTests(flask_testing.TestCase):


    def create_app(self):
        return app
    
    def testOne(self):
        response=self.client.get('/',content_type='html/text')
        self.assertEqual(response.status,'404 NOT FOUND')

    def test_get(self):
        with app.test_client() as test_client:
            response=test_client.get('/pedidos')
            self.assertEqual(response.status_code,200)
    
    def test_post(self):
        with app.test_client() as test_client:
            response=test_client.post('/pedidos', data=dict(
            id =1,
            id_cliente =1,
            id_producto =1,
            cantidad =1,
            nom_product ="1",
            precio_uni =1,
            precio_tot =1)
            )
        self.assertEqual(response.status_code,200)
    
        
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