from django.db import models

# Create your models here.
class Person(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=256)
    phone = models.CharField(max_length=256, null=True)
    #accountType = models.ForeignKey('freeOrPaid.Pricing', null=True)
    accountType = models.CharField(max_length=50, default="free")    
    joinDate = models.DateField(blank=True, null=True)    
