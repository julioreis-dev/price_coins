from rest_framework import serializers
from cotacao.models.cotacaomodel import Cotacoes


class CotacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotacoes
        fields = '__all__'