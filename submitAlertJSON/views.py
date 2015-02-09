
from django.shortcuts import render
from registerJSON.models import Person
from submitAlertJSON.models import Alert, NumAlertsPerPerson
from json import dumps
import time
from hashlib import sha224
# Create your views here.
from django.http import HttpResponse

def index(request):

    if request.session.get('has_loggedin',False):
        emailGet = request.session.get('email',False)
        returnDict = {}

        numAlerts = NumAlertsPerPerson.objects.get(person=emailGet)
        if numAlerts.numAlerts == numAlerts.maxAlerts:
            returnDict['success'] = -2
            return HttpResponse(dumps(returnDict))
        priceThresholdPost = request.POST.get("priceThreshold")
        signPost = request.POST.get("sign")
        emailAlertPost = request.POST.get("emailAlert")
        if emailAlertPost == 'false':
            emailAlertPost = False
        textAlertPost = request.POST.get("textAlert")
        if textAlertPost == 'false':
            textAlertPost=False
        timeIntervalNumPost = request.POST.get("timeIntervalNum")
        timeIntervalUnitPost = request.POST.get("timeIntervalUnit")
        exchangePost = request.POST.get("exchange")

        
        personGet = Person.objects.get(email=emailGet)
        alertIDTemp = sha224(emailGet+str(int(time.time()))).hexdigest()
        alertToAdd = Alert.objects.create(person=personGet, email=emailGet, alertID=alertIDTemp)
        alertToAdd.priceThreshold=priceThresholdPost
        alertToAdd.sign = signPost
        alertToAdd.emailAlert = emailAlertPost
        alertToAdd.textAlert = textAlertPost
        intervalInSecondsCalc = float(timeIntervalNumPost)
        if timeIntervalUnitPost == 'day':
            intervalInSecondsCalc *=86400
        elif timeIntervalUnitPost == 'hour':
            intervalInSecondsCalc *=3600
        else:
            intervalInSecondsCalc *= 60
        alertToAdd.intervalInSeconds = intervalInSecondsCalc
        alertToAdd.exchange = exchangePost
        alertToAdd.save()
        numAlerts.numAlerts += 1
        numAlerts.save()
        returnDict['success']=1
        return HttpResponse(dumps(returnDict))
    else:
        returnDict = {}
        returnDict['success']=-1
        return HttpResponse(dumps(returnDict))
