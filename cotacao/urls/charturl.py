from django.urls import path
from cotacao.actions.chart import dataview

app_name = 'chart'
urlpatterns = [
    path('', dataview, name='index'),
]
