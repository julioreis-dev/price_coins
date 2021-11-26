from django.db import models
from django.utils import timezone


class Cotacoes(models.Model):
    date = models.DateField(default=timezone.now())
    coin = models.CharField(max_length=50, blank=True, null=True)
    values = models.FloatField(default=0)

    def __str__(self):
        return f'{self.date}_{self.coin}'

