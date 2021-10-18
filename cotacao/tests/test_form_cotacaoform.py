from django.test import TestCase
from cotacao.forms.cotacao import CotacoesForm
from model_mommy import mommy
from datetime import datetime


class CotacoesFormTest(TestCase):
    def setUp(self):
        self.inst = mommy.make('Cotacoes')
        self.inst.date = datetime.now().date()
        self.data = {
            'date': self.inst.date,
            'coin': self.inst.coin,
        }

    def test_form(self):
        form = CotacoesForm(data=self.data)
        form.is_valid()
        self.assertEquals(form.cleaned_data['date'], self.data['date'])
        self.assertEquals(form.cleaned_data['coin'], self.data['coin'])
