from rest_framework import viewsets
from rest_framework.views import APIView
from cotacao.models.cotacaomodel import Cotacoes
from .serializers import CotacaoSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class CotacaoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CotacaoSerializer
    queryset = Cotacoes.objects.all()


class CoinViewSet(APIView):
    serializer_class = CotacaoSerializer

    def get_object(self, name):
        try:
            return Cotacoes.objects.filter(coin=name).all()
        except Cotacoes.DoesNotExist:
            raise Http404

    def get(self, name):
        coin = self.get_object(name)
        serializer = CotacaoSerializer(coin, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class DateViewSet(APIView):
    serializer_class = CotacaoSerializer

    def get_object(self, date):
        try:
            return Cotacoes.objects.filter(date=date).all()
        except Cotacoes.DoesNotExist:
            raise Http404

    def get(self, request, date):
        date = self.get_object(date)
        serializer = CotacaoSerializer(date, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        # return Response(serializer.data)


class MixViewSet(APIView):
    serializer_class = CotacaoSerializer

    def get_object(self, name, date):
        try:
            return Cotacoes.objects.filter(coin=name, date=date).all()
        except Cotacoes.DoesNotExist:
            raise Http404

    def get(self, request, name, date, format=None):
        mix = self.get_object(name, date)
        serializer = CotacaoSerializer(mix, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
