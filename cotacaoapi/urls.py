from django.urls import path, include
from .views import CotacaoViewSet, CoinViewSet, DateViewSet, MixViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('cotacao', CotacaoViewSet, basename='cotacao')


urlpatterns = [
    path('', include(router.urls)),
    path('coin/<str:name>/', CoinViewSet.as_view(), name='coin'),
    path('date/<str:date>/', DateViewSet.as_view(), name='date'),
    path('result/<str:name>&<str:date>/', MixViewSet.as_view(), name='mix'),
    ]
