import unittest

from yargy import Parser
from Adress import ADDRESS_RULE

class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = Parser(ADDRESS_RULE)

    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual( 'проспект комсомольский', res.street)

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('улица катукова', res.street)

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('улица рабочая', res.street)

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('доватора', res.street)

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('бехтеева', res.street)

    def test_6(self):
        testing_address = 'улица меркулова дом 24'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('улица меркулова', res.street)

    def test_7(self):
        testing_address = 'октябрьская 48 частный дом город сургут'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('октябрьская', res.street)

    def test_8(self):
        testing_address = 'сколько улица 30 лет победы 50 46'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('улица 30 лет победы', res.street)

    def test_9(self):
        testing_address = 'тюменский тракт 10'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('тюменский тракт', res.street)

    def test_10(self):
        testing_address = 'сургут югорская 30/2'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('югорская', res.street)

    def test_11(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        res = self.NERInstance.find(testing_address)
        self.assertEqual(None, res)

    def test_12(self):
        testing_address = 'старый оскол микрорайон олимпийский дом 23 квартира 105'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('микрорайон олимпийский', res.street)

    def test_13(self):
        testing_address = 'город сургут улица фармана салманова 4'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('улица фармана салманова', res.street)

    def test_14(self):
        testing_address = 'ты сургут улица 30 лет победы'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('улица 30 лет победы', res.street)

    def test_15(self):
        testing_address = 'проезд мунарева 2'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('проезд мунарева', res.street)

    def test_16(self):
        testing_address = 'домашний адрес где я живу'
        res = self.NERInstance.find(testing_address)
        self.assertEqual( None, res)

    def test_17(self):
        testing_address = 'артема 32 квартира 8'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('артема', res.street)

    def test_18(self):
        testing_address = 'знаете знаете у меня дорогая девочка у меня уже все есть и менять из из одного переходить на другой я не хочу поэтому какой город квартира какой ничего я вам сообщать не хочу поэтому до свидания я ничего не'
        res = self.NERInstance.find(testing_address)
        self.assertEqual(None, res)

    def test_19(self):
        testing_address = 'новогиреевская 34'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('новогиреевская', res.street)

    def test_20(self):
        testing_address = 'мое 3 парковая'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('парковая', res.street)

    def test_21(self):
        testing_address = 'москва мусы джалиля 38 корпус 2'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('мусы джалиля', res.street)

    def test_22(self):
        testing_address = 'надо 50% город нальчик горького 1257'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('горького', res.street)

    def test_23(self):
        testing_address = 'сколько стоит нет arkadata у нас есть москва каширское шоссе 55 корпус 1'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('каширское шоссе', res.street)

    def test_24(self):
        testing_address = 'зеленые аллеи город видное дом 8'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('зеленые аллеи', res.street)

    def test_25(self):
        testing_address = 'дмитрия ульянова 17 корпус 1 москва'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('дмитрия ульянова', res.street)

    def test_26(self):
        testing_address = 'null'
        res = self.NERInstance.find(testing_address)
        self.assertEqual(None, res)

    def test_27(self):
        testing_address = 'стол вы знаете москва алтуфьевское 78'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('алтуфьевское', res.street)

    def test_28(self):
        testing_address = 'марша захарова 12 маршала захарова дом 12'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('маршала захарова', res.street)

    def test_29(self):
        testing_address = 'а зачем'
        res = self.NERInstance.find(testing_address)
        self.assertEqual(None, res)

    def test_30(self):
        testing_address = 'Кавказский 16'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('Кавказский', res.street)

    def test_31(self):
        testing_address = 'Старый Гай 1 корпус 2'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('Старый Гай'.lower(), res.street.lower())

    def test_32(self):
        testing_address = 'зелинского улица зелинского дом 2'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('улица зелинского', res.street)


if __name__ == '__main__':
    unittest.main()
