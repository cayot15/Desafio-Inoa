from django.db import models
# Create your models here.


class Closeprice(models.Model):
    data = models.DateField()
    valordefecho = models.FloatField()


class Stock(models.Model):
    nome = models.CharField(max_length=255)
    frequencia = models.CharField(max_length=255,null='1m')
    ticker = models.CharField(max_length=255, null='1m')
    precomax = models.FloatField()
    precomin = models.FloatField()
    lastprice=models.FloatField(null=True)