import os
import mtg
import unittest
import tempfile
import json
import requests

class mtgTestCase(unittest.TestCase):
    def setUp(self):
        mtg.app.config['TESTING'] = True
        self.app = mtg.app.test_client()
        
    def test_get_card(self):
        data = {'name': 'Llanowar Elves'}
#schema is http:
        r = self.app.get('/search_cards/', "contedata))
   #     r = requests.get(self)
        print r.text
       # assert "" in response.data
    
if __name__ == '__main__':
    unittest.main()
    
