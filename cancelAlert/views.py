from submitAlertJSON.models import Alert, NumAlertsPerPerson
# Create your views here.
from django.http import HttpResponse
from json import dumps
from django.shortcuts import render

def index(request, alertIDTemp):
    returnDict={}    
    try:
        alertToDelete = Alert.objects.get(alertID=alertIDTemp)
        person = alertToDelete.person_id
        numAlerts = NumAlertsPerPerson.objects.get(person_id=person)
        numAlerts.decreaseActiveAlerts()
        numAlerts.save()
        alertToDelete.delete()
        returnDict['success'] = 1
        returnDict['message'] = 'Successfully deleted alert'
        return HttpResponse(dumps(returnDict))        
    except Alert.DoesNotExist:
        returnDict['success'] = -2
        returnDict['message'] = 'Alert does not exist'
        return HttpResponse(dumps(returnDict))

def cancelPage(request, alertIDTemp):
    try:
        alertToDelete = Alert.objects.get(alertID=alertIDTemp)
        person = alertToDelete.person_id
        numAlerts = NumAlertsPerPerson.objects.get(person_id=person)
        numAlerts.decreaseActiveAlerts()
        numAlerts.save()
        alertToDelete.delete()
        return render(request, 'index.html', {'hiddenVar':' ', 'alertMessage':'Successfully canceled alert'})     
    except Alert.DoesNotExist:
        return render(request, 'index.html', {'hiddenVar':' ', 'alertMessage':'Unsuccessfully canceled alert'})  
