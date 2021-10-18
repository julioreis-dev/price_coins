from django.urls import path
from cotacao.views.home import IndexTemplateView
from cotacao.views.cotacao import upload_cotation

app_name = 'home'

urlpatterns = [path('', IndexTemplateView.as_view(), name='index'),
               ]
