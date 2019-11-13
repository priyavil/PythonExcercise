#StarWarsTest.py
import unittest
from StarWars import ApiHelper

class Test_StarWars(unittest.TestCase):
    def setUp(self):
        self.StarWarObj = ApiHelper()


    # Returns True if the string contains 4 a.
    def test_nonEmptyArray(self):
        print(self._testMethodName)
        url = "https://swapi.co/api/people/"
        #call the method and get the list of values
        listOfChar = self.StarWarObj.star_wars_characters(url)
        #Check whether it returns empy or not
        self.assertTrue( len(listOfChar) > 0)


if __name__ == '__main__':
    unittest.main()
