
from django.shortcuts import render
from registerJSON.models import Person
from django.template.defaulttags import csrf_token
from django.http import HttpResponse
from json import dumps
from submitAlertJSON.models import Alert, NumAlertsPerPerson
# Create your views here.

def index(request):
    
    returnDict = {}
    emailGet = request.session.get('email',False)
    if request.session.get('has_loggedin',False):
        alerts = getAlerts(emailGet)
        returnDict['success'] = 1
        returnDict['data'] = alerts
        return HttpResponse(dumps(returnDict))
        
    else:
        returnDict['success'] = 'not logged in'
        return HttpResponse(dumps(returnDict))


def getAlerts(emailTemp):
    allAlerts = Alert.objects.filter(email=emailTemp)
    alertList = []
    for alert in allAlerts:
        alertTemp = {}
        alertTemp['priceThreshold'] = alert.priceThreshold
        alertTemp['sign'] = alert.sign
        alertTemp['intervalInSeconds'] = alert.intervalInSeconds
        alertTemp['emailAlert'] = alert.emailAlert
        alertTemp['textAlert'] = alert.textAlert
        alertTemp['exchange'] = alert.exchange
        alertTemp['alertID'] = alert.alertID
        alertList.append(alertTemp)

    return alertList

def getNumAlerts(request):
    emailGet = request.session.get('email',False)
    returnDict = {}
    if request.session.get('has_loggedin',False):    
        numAlertsObj=NumAlertsPerPerson.objects.get(person_id=emailGet)
        returnDict['success'] = 1
        returnDict['numAlerts'] = numAlertsObj.numAlerts
        returnDict['maxAlerts'] = numAlertsObj.maxAlerts
        return HttpResponse(dumps(returnDict))
    else:
        returnDict['success'] = -1
        return HttpResponse(dumps(returnDict))
