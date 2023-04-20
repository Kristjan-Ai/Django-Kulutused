from django.db import models

# Create your models here.

class inimene(models.Model):
    nimi = models.CharField(max_length=200)
    raha = models.DecimalField(max_digits=200, decimal_places=2)
    def __str__(self):
        return self.nimi
class tehing(models.Model):
    saaja = models.CharField(max_length=200)
    andja = models.CharField(max_length=200)
    kogus = models.DecimalField(max_digits=200, decimal_places=2)
    selgitus = models.CharField(default="Selgitus puudub.", max_length=10000)
    def __self__(self):
        return self.saaja+" --> "+self.andja