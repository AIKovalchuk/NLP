import unittest

from yargy          import Parser
from Adress         import ADDRESS_RULE

class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = Parser(ADDRESS_RULE)

    def test_shkolnaya(self):
        testing_address = 'петербург школьная 20'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('петербург', res.city)
        self.assertEqual('школьная', res.street)
        self.assertEqual('20', res.house)

    def test_full_gagarina(self):
        testing_address = 'петербург юрия гагарина 22 к2'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('петербург', res.city)
        self.assertEqual('юрия гагарина', res.street)
        self.assertEqual('22', res.house)
        self.assertEqual('к2', res.part)

    def test_short_gagarina(self):
        testing_address = 'питер гагарина 22 к2'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('гагарина', res.street)
        self.assertEqual('22', res.house)
        self.assertEqual('к2', res.part)

    def test_untolovsky(self):
        testing_address = "санкт-петербург;юнтоловский 43 корпус 1"
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('петербург', res.city)
        self.assertEqual('юнтоловский', res.street)
        self.assertEqual('43', res.house)
        self.assertEqual('корпус 1', res.part)


    def test_untolovsky_str(self):
        testing_address = "санкт-петербург;юнтоловский 43 строение 1"
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('петербург', res.city)
        self.assertEqual('юнтоловский', res.street)
        self.assertEqual('43 1', res.house)
        self.assertEqual('строение 1', res.building)

    def test_untolovsky_str(self):
        testing_address = "юнтоловский 43 ст 1"
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('юнтоловский', res.street)
        self.assertEqual('43', res.house )
        self.assertEqual('ст 1', res.building )

if __name__ == '__main__':
    unittest.main()
