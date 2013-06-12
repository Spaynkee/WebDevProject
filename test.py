import os
import mtg
import unittest
import tempfile
import json

class mtgTestCase(unittest.TestCase):
    def setUp(self):
        mtg.app.config['TESTING'] = True
        self.app = mtg.app.test_client()
        
    def testGetCard(self):
        rv = self.app.get('/getCard')
        data = {'name': 'Llanowar Elves'}
        json_data = json.dumps(data)
        response = self.app.post('/getCard', data)
		print json_data
        assert json_data in rv.data
    
if __name__ == '__main__':
    unittest.main()
    
