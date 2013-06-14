from ast import literal_eval
import mtg
import unittest
import requests
import json


class mtgTestCase(unittest.TestCase):

    def setUp(self):
        mtg.app.config['TESTING'] = True
        self.app = mtg.app.test_client()

    def tearDown(self):
        # I don't have anything to tear down yet
        pass

    def testSearchCards(self):
        # should return many cards
        rv = self.app.get('/search_cards?pyCardName=%s' % 'llanowar', follow_redirects=True)
        self.assertIn('Llanowar~', rv.data, "llanowar didn't return search results... interesting")

        # should return 1 card
        rv = self.app.get('/search_cards?pyCardName=%s' % 'Dark Sphere', follow_redirects=True)
        self.assertIn('Dark Sphere~', rv.data, "Dark Sphere didn't return search results... interesting")

        # should return 0 cards
        rv = self.app.get('/search_cards?pyCardName=%s' % 'ghawue', follow_redirects=True)
        self.assertNotIn('ghawue~', rv.data, "You searched for 'ghawue'  and got results? PERPOSTEROUS!")

        # should return nothing, as nothing was searched for
        rv = self.app.get('/search_cards?pyCardName=%s' % '', follow_redirects=True)
        self.assertEquals(rv.data, "", "You searched for '' and got results? PERPOSTEROUS!")

    def testGetCard(self):
        #if told to get a string with multiple versions/cards
        rv = self.app.get('/get_card?pyCardName=%s' % 'swamp', follow_redirects=True)
        results = json.loads(rv.data)
        self.assertEqual(results['name'], "Swamp", )

        #if told to get a string with '' entered.
        results = {}
        rv = self.app.get('/get_card?pyCardName=%s' % '', follow_redirects=True)
        try:
            results = json.loads(rv.data)
        except:
            self.assertEqual(results['name'], "", )

        #if told to get a string with one 1 card/result
        rv = self.app.get('/get_card?pyCardName=%s' % 'Kavu Predator', follow_redirects=True)
        results = json.loads(rv.data)
        self.assertEqual(results['name'], "Kavu Predator", )

        #if told to get string with with no results.
        results = {}
        rv = self.app.get('/get_card?pyCardName=%s' % 'wafawwe', follow_redirects=True)
        print rv.data
        try:
            results = json.loads(rv.data)
            self.assertEqual(results['name'], "", )
        except ValueError:
            self.assertIs(rv.data, '', "You searched for 'wafawwe' and got results? PERPOSTEROUS!")

if __name__ == '__main__':
    unittest.main()
