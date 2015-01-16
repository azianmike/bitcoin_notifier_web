from django.db import models

# Create your models here.
class Pricing(models.Model):
    status = models.CharField(max_length=100, default="free", primary_key=True)
    price = models.IntegerField(default="0")
    numOfAlerts = models.IntegerField(default="1")
