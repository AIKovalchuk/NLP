import unittest

from yargy import Parser
from Adress import ADDRESS_RULE

class TestHome(unittest.TestCase):
    def setUp(self):
        self.NERInstance = Parser(ADDRESS_RULE)

    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual(res.house, '50')

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual(res.house, '36 a')

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual(res.house, '31а')

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual(res.house, '18')

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual(res.house, '9')

    def test_6(self):
        testing_address = 'артема 32 квартира 8'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual(res.house, '32')

    def test_7(self):
        testing_address = 'город липецк полиграфическая дом 4'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual(res.house, '4')

    def test_8(self):
        testing_address = 'сколько стоит нет arkadata у нас есть москва каширское шоссе 55 корпус 1'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual(res.house, '55 1', )

    def test_9(self):
        testing_address = 'люберцы октябрьский проспект 10 корпус 1'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual(res.house, '10 1')

    def test_10(self):
        testing_address = 'бульвар миттова 24'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual(res.house, '24')

    def test_11(self):
        testing_address = 'стол вы знаете москва алтуфьевское 78'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual(res.house, '78')


if __name__ == '__main__':
    unittest.main()
