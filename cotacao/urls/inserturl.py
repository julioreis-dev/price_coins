from django.urls import path
from cotacao.views.cotacao import upload_cotation

app_name = 'insert'
urlpatterns = [path('', upload_cotation, name='insert'),]