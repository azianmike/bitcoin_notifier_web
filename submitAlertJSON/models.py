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

    def updateNextAlert(self):
        import time        
        self.nextAlert = int(time.time()) + self.intervalInSeconds 
        super(Alert, self).save()

    def deleteAlert(self):
        temp = NumAlertsPerPerson.objects.get(person=self.person)
        temp.decreaseActiveAlerts()
        temp.save()
        self.delete()
    

class NumAlertsPerPerson(models.Model):
    person = models.ForeignKey('registerJSON.Person', primary_key=True)
    numAlerts = models.IntegerField(default=0)
    maxAlerts = models.IntegerField(default=5)
    
    def decreaseActiveAlerts(self):
        if self.numAlerts==0:
            return
        self.numAlerts -= 1
    
    def increaseActiveAlerts(self):
        if self.numAlerts==self.maxAlerts:
            return
        
        self.numAlerts += 1

class AlertsPerHour(models.Model):
    lastHour = models.IntegerField(default=0)
    alertsSentInLastHour = models.IntegerField(default=0)
    person = models.ForeignKey('registerJSON.Person', primary_key=True)
