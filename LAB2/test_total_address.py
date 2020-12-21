import unittest

from yargy import Parser
from Adress import ADDRESS_RULE

class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = Parser(ADDRESS_RULE)

    def test_one(self):
        testing_address = 'проспект комсомольский 50'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('проспект комсомольский', res.street)
        self.assertEqual('50', res.house)


    def test_second(self):
        testing_address = 'город липецк улица катукова 36 a'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('город липецк', res.city)
        self.assertEqual('улица катукова', res.street)
        self.assertEqual('36 a', res.house)


    def test_third(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('сургут', res.city)
        self.assertEqual('улица рабочая', res.street)
        self.assertEqual('дом 31а', res.house)


    def test_fouth(self):
        testing_address = 'город липецк доватора 18'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('город липецк', res.city)
        self.assertEqual('доватора', res.street)
        self.assertEqual('18', res.house)

    def test_behtereva(self):
        testing_address =  'ну бехтеева 9 квартира 310'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('бехтеева',res.street)
        self.assertEqual('9',  res.house)
        self.assertEqual('310', res.appartment )

    def test_moskovskaya(self):
        testing_address =  'московская 34б'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('московская', res.street,)
        self.assertEqual('34б', res.house)

    def test_minina(self):
        testing_address =  'улица минина дом 1'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('улица минина', res.street)
        self.assertEqual('дом 1', res.house)

    def test_30_let_victory(self):
        testing_address =  'сколько улица 30 лет победы 50 46'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('улица 30 лет победы', res.street)
        self.assertEqual( '50', res.house)
        self.assertEqual('46', res.appartment)

    def test_tract(self):
        testing_address =  'тюменский тракт 10'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('тюменский тракт', res.street )
        self.assertEqual('10', res.house )

    def test_beregovaya(self):
        testing_address =  'береговая 43 береговая 43 сургут'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('сургут', res.city)
        self.assertEqual('береговая', res.street)
        self.assertEqual( '43', res.house)

    def test_yuogorskaya(self):
        testing_address =  'сургут югорская 30/2'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('сургут', res.city)
        self.assertEqual('югорская', res.street)
        self.assertEqual('30/2', res.house)

    def test_index(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        res = self.NERInstance.find(testing_address)
        self.assertEqual(None, res )

    def test_salmanova(self):
        testing_address = 'город сургут улица фармана салманова 4'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('город сургут', res.city, )
        self.assertEqual('улица фармана салманова', res.street, )
        self.assertEqual('4', res.house, )

    def test_vidnoe(self):
        testing_address = 'зеленые аллеи город видное дом 8'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('город видное', res.city, )
        self.assertEqual( 'зеленые аллеи', res.street,)
        self.assertEqual('дом 8', res.house )

    def test_zelinskogo(self):
        testing_address = 'зелинского улица зелинского дом 2'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('улица зелинского', res.street, )
        self.assertEqual('дом 2', res.house )

    def test_kuskovaya_corpus(self):
        testing_address = 'Кусковская 19 корпус 1 '
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('Кусковская', res.street, )
        self.assertEqual('19', res.house, )
        self.assertEqual('корпус 1', res.part )
        self.assertEqual(None, res.appartment )

    def test_shosse(self):
        testing_address = 'москва щелковское шоссе 35'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('москва', res.city, )
        self.assertEqual('щелковское шоссе', res.street, )
        self.assertEqual('35', res.house, )

    def test_park(self):
        testing_address = 'город москва марьинский парк дом 25 корпус 2'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual( 'город москва', res.city,)
        self.assertEqual( 'марьинский парк', res.street,)
        self.assertEqual('дом 25', res.house, )

    def test_gai(self):
        testing_address = 'Старый Гай 1 корпус 2'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('Старый Гай'.lower(), res.street.lower())
        self.assertEqual('1', res.house)

    def test_third_post(self):
        testing_address = 'улица 3 почтовое отделение дом 62'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('улица 3 почтовое отделение', res.street, )
        self.assertEqual('дом 62', res.house, )

    def test_july_street(self):
        testing_address = 'нижний новгород улица июльских дней 19'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual( 'нижний новгород', res.city,)
        self.assertEqual('улица июльских дней', res.street, )
        self.assertEqual('19', res.house, )

    def test_val(self):
        testing_address = 'так москва хамовнический вал но я думаю что я еще обсужу со своими домашними то есть вот у нас цифровое телевидение есть но акадо вот вы не спешите я тогда вам наберу но либо в приложения'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('москва', res.city, )
        self.assertEqual('хамовнический вал', res.street, )

    def test_semen_bilecky(self):
        testing_address = 'город сургут улица семена билецкого 1'
        res = self.NERInstance.find(testing_address).fact
        self.assertEqual('город сургут', res.city,)
        self.assertEqual('улица семена билецкого', res.street, )
        self.assertEqual('1', res.house, )


    def test_critical(self):
        testing_address = 'улица значит антонова овсиенко дом 19/2'
        res = self.NERInstance.find(testing_address).fact
        print(testing_address, res)
        self.assertEqual('антонова овсиенко', res.street )
        self.assertEqual('19/2', res.house, )

    def test_critical0(self):
        testing_address = 'улица генерала армии епишева дом 9'
        res = self.NERInstance.find(testing_address).fact
        print(testing_address, res)
        self.assertEqual('улица генерала армии епишева', res.street )
        self.assertEqual('дом 9', res.house, )


    def test_critical1(self):
        testing_address = 'улица академика байкова дом 9'
        res = self.NERInstance.find(testing_address).fact
        print(testing_address, res)
        self.assertEqual('дом 9', res.house, )
        self.assertEqual('улица академика байкова', res.street )

    def test_critical2(self):
        testing_address = 'улица академика байкова дом дом дом 9'
        res = self.NERInstance.find(testing_address).fact
        print(testing_address, res)
        self.assertEqual('дом9', res.house, )
        self.assertEqual(('академика байкова', 'улица'), res.street )

    def test_critical2_3(self):
        testing_address = 'улица подзаборного байкова дом дом дом 9'
        res = self.NERInstance.find(testing_address).fact
        print(testing_address, res)
        self.assertEqual('дом 9', res.house, )
        self.assertEqual('улица подзаборного байкова', res.street )

    def test_critical2_4(self):
        testing_address = 'улица монтажника байкова дом дом дом 9'
        res = self.NERInstance.find(testing_address).fact
        print(testing_address, res)
        self.assertEqual('дом 9', res.house)
        self.assertEqual('улица монтажника байкова', res.street )

    def test_critical3(self):
        testing_address = 'такзначит у меня дом номер 12 а улица джона рида'
        res = self.NERInstance.find(testing_address).fact
        print(testing_address, res)
        self.assertEqual('улица джона рида', res.street)
        self.assertEqual('дом 12', res.house )

if __name__ == '__main__':
    unittest.main()