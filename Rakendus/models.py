from django.db import models
import django

# Create your models here.

class tehing(models.Model):
    saaja = models.CharField(max_length=200)
    andja = models.CharField(max_length=200)
    kogus = models.DecimalField(max_digits=200, decimal_places=2)
    selgitus = models.CharField(default="Selgitus puudub.", max_length=10000)
    aeg = models.DateTimeField("Tehingu toimumise aeg", default=django.utils.timezone.now)
    def __str__(self):
        return self.saaja+" --> "+self.andja+" id:"+str(self.id)