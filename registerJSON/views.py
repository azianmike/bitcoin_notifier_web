from django.shortcuts import render
from registerJSON.models import Person
from submitAlertJSON.models import NumAlertsPerPerson
from django.template.defaulttags import csrf_token
from json import dumps
import datetime
from hashlib import sha224
# Create your views here.
from django.http import HttpResponse

def index(request):
    emailPost = request.POST.get("email", "")
    phonePost = request.POST.get("phone")
    passwordPost = request.POST.get("password", "")
    returnDict = {}
    try:
        checkOld = Person.objects.get(email=emailPost)
        returnDict['success']=0
        return HttpResponse(dumps(returnDict))
    except Person.DoesNotExist:
        f='%Y-%m-%d'
        now = datetime.datetime.now()
        mysqlTime = now.strftime(f)
        activateCodeTemp = sha224(emailPost+"randomWord").hexdigest()
        userToAdd = Person.objects.create(email=emailPost, password=passwordPost,joinDate=mysqlTime, activateCode=activateCodeTemp)    
        userToAdd.phone = phonePost
        userToAdd.save()
        tempNumAlerts = NumAlertsPerPerson.objects.create(person=userToAdd)
        returnDict['success']=1
        return HttpResponse(dumps(returnDict))

def activate(request, activationID):
    personToActivate = Person.objects.get(activateCode=activationID)
    personToActivate.activated = True
    personToActivate.save()
    return HttpResponse("activated")
