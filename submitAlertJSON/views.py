
from django.shortcuts import render
from registerJSON.models import Person
from submitAlertJSON.models import Alert
from json import dumps
# Create your views here.
from django.http import HttpResponse

def index(request):

    if request.session.get('has_loggedin',False):
        emailGet = request.session.get('email',False)
        priceThresholdPost = request.POST.get("priceThreshold")
        signPost = request.POST.get("sign")
        emailAlertPost = request.POST.get("emailAlert")
        textAlertPost = request.POST.get("textAlert")
        timeIntervalNumPost = request.POST.get("timeIntervalNum")
        timeIntervalUnitPost = request.POST.get("timeIntervalUnit")
        exchangePost = request.POST.get("exchange")

        returnDict = {}
        personGet = Person.objects.get(email=emailPost)
        alertToAdd = Alert.objects.create(person=personGet, email=emailGet)
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
        returnDict['success']=1
        return HttpResponse(dumps(returnDict))
    else:
        returnDict = {}
        returnDict['success']=-1
        return HttpResponse(dumps(returnDict))
