from django.test import TestCase, Client


class CotacaoViewSetTest(TestCase):
    def setUp(self):
        self.cotacao = 'cotacao'
        self.client = Client()

    def test_api(self):
        response = self.client.get(f'/api/{str(self.cotacao)}/')
        self.assertEqual(response.status_code, 200)


class CoinViewSetTest(TestCase):
    def setUp(self):
        self.coin = 'EUR'
        self.client = Client()

    def test_api(self):
        response = self.client.get(f'/api/coin/{str(self.coin)}/')
        self.assertEqual(response.status_code, 200)


class DateViewSetTest(TestCase):
    def setUp(self):
        self.date = '2021-05-10'
        self.client = Client()

    def test_api(self):
        response = self.client.get(f'/api/date/{str(self.date)}/')
        self.assertEqual(response.status_code, 200)


class MixViewSetTest(TestCase):
    def setUp(self):
        self.coin = 'BRL'
        self.date = '2021-05-10'
        self.client = Client()

    def test_api(self):
        response = self.client.get(f'/api/result/{str(self.coin)}&{str(self.date)}/')
        self.assertEqual(response.status_code, 200)
