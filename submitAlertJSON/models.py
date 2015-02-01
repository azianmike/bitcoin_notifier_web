from django.db import models

# Create your models here.
class Alert(models.Model):
    alertID = models.CharField(max_length=200, primary_key=True)
    email = models.CharField(max_length=100, default="test")    
    person = models.ForeignKey('registerJSON.Person')
    phone = models.CharField(max_length=20, null=True)
    priceThreshold = models.IntegerField(default="12")
    sign = models.CharField(max_length=20, default="12")
    nextAlert = models.IntegerField(default="10")
    intervalInSeconds = models.IntegerField(default="1000000")
    emailAlert = models.BooleanField(default=False)
    textAlert = models.BooleanField(default=False)
    exchange = models.CharField(max_length=100, default="coinbase")

class NumAlertsPerPerson(models.Model):
    person = models.ForeignKey('registerJSON.Person', primary_key=True)
    numAlerts = models.IntegerField(default=0)
    maxAlerts = models.IntegerField(default=1)
