import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr.bk1 import create_app
from models import setup_db


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        # self.database_name = "trivia_test"
        self.database_path ='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='ks8pa75ol3h0skzv',
 password='el5w7f3rjcbisebg', server='z3iruaadbwo0iyfp.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306', database='jwjgkj993t2yf6sa')

        setup_db(self.app, self.database_path)
        self.new_question = {'question': 'HEt?', 'answer':'Yes man', 'category':'self', 'difficulty':5}
        # binds the app to the current context
        # with self.app.app_context():
        #     self.db = SQLAlchemy()
        #     self.db.init_app(self.app)
        #     # create all tables
        #     self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_if_all_works(self):
        res = self.client().get("/save")
        json = res.data
        print(json)
        self.assertEqual(res.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()