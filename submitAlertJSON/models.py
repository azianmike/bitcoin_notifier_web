from django.db import models

# Create your models here.
class Alert(models.Model):
    email = models.CharField(max_length=100, default="test")    
    person = models.ForeignKey('registerJSON.Person', primary_key=True)
    phone = models.CharField(max_length=20, null=True)
    priceThreshold = models.IntegerField(default="12")
    sign = models.CharField(max_length=20, default="12")
    lastAlert = models.DateField(blank=True, null=True)
    intervalInSeconds = models.IntegerField(default="1000000")
    emailOrText = models.CharField(max_length=50, default="email")
