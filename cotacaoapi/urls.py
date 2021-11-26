from django.urls import path, include
from .views import CotacaoViewSet, CoinViewSet, DateViewSet, MixViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('cotacao', CotacaoViewSet, basename='cotacao')


urlpatterns = [
    path('', include(router.urls)),
    path('coin/<str:name>/', CoinViewSet.as_view(), name='apicoin'),
    path('date/<str:date>/', DateViewSet.as_view(), name='apidate'),
    # path('result&coin=<str:name>&date=<str:date>/', MixViewSet.as_view(), name='apimix'),
    # path('result/coin=<str:name>&date=<str:date>/', MixViewSet.as_view(), name='apimix'),
    ]
