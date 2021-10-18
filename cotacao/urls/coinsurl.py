from django.urls import path
from cotacao.views.menu import CoinsTemplateView

app_name = 'coin'
urlpatterns = [path('', CoinsTemplateView.as_view(), name='menu'),

               ]
