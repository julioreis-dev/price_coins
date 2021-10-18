from django.test import TestCase
from cotacao.models.cotacaomodel import Cotacoes
from model_mommy import mommy


class CotacaoModelTest(TestCase):
    def setUp(self):
        self.cotacao = mommy.make('Cotacoes')

    def test_cotacao_exist(self):
        cotacao = Cotacoes.objects.first()
        self.assertIsNotNone(cotacao)

    def test_str(self):
        attrstr = f'{self.cotacao.date}_{self.cotacao.coin}'
        self.assertEquals(str(self.cotacao), attrstr)
