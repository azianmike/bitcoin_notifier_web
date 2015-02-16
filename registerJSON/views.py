from django.shortcuts import render
from registerJSON.models import Person
from submitAlertJSON.models import NumAlertsPerPerson
from django.template.defaulttags import csrf_token
from json import dumps
import datetime
from hashlib import sha224
# Create your views here.
from django.http import HttpResponse
from sentActivationEmail import sendActivationEmail


def index(request):
    emailPost = request.POST.get("email", "")
    phonePost = request.POST.get("phone")
    passwordPost = request.POST.get("password", "")
    returnDict = {}
    if not request.session.get('store_cookie',False):
        returnDict['success'] = -1
        return HttpResponse(dumps(returnDict))
    try:
        checkOld = Person.objects.get(email=emailPost)
        returnDict['success']=0
        returnDict['message']="Email is already registered!"
        return HttpResponse(dumps(returnDict))
    except Person.DoesNotExist:
        f='%Y-%m-%d'
        now = datetime.datetime.now()
        mysqlTime = now.strftime(f)
        activateCodeTemp = sha224(emailPost+"randomWord").hexdigest()
        sendActivationEmail(emailPost, activateCodeTemp)
        userToAdd = Person.objects.create(email=emailPost, password=passwordPost,joinDate=mysqlTime, activateCode=activateCodeTemp)    
        userToAdd.phone = phonePost
        userToAdd.save()
        tempNumAlerts = NumAlertsPerPerson.objects.create(person=userToAdd)
        returnDict['success']=1
        returnDict['message'] = "Registered! Check your email to activate your account"
        return HttpResponse(dumps(returnDict))

def activate(request, activationID):
    from django.shortcuts import render
    personToActivate = Person.objects.get(activateCode=activationID)
    personToActivate.activated = True
    personToActivate.save()
    return render(request, 'index.html', {'hiddenVar':'', 'alertMessage':'Successfully activated account'})  
