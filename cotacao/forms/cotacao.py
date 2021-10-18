from django import forms
from cotacao.models.cotacaomodel import Cotacoes


class CotacoesForm(forms.ModelForm):
    class Meta:
        model = Cotacoes
        fields = ['date', 'coin']
