from django.test import TestCase
from cotacao.actions.controlers import read_api


class ReadApiTest(TestCase):
    def test_read_api(self):
        expected = [['2014-04-16', 'BRL', 2.23], ['2014-04-16', 'EUR', 0.72], ['2014-04-16', 'JPY', 102.28]]
        real = read_api('2014-04-16')
        self.assertEqual(real, expected)
