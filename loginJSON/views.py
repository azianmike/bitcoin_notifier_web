from django.shortcuts import render
from registerJSON.models import Person
from django.template.defaulttags import csrf_token
from django.http import HttpResponse
from json import dumps
# Create your views here.

def index(request):
    emailPost = request.POST.get("email", "")
    passwordPost = request.POST.get("password", "")
    returnDict = {}
    returnDict['success'] = -1
    if request.session.get('has_loggedin',False):
        returnDict['success'] = -2
        return HttpResponse(dumps(returnDict))    

    try:
        checkOld = Person.objects.get(email=emailPost, password=passwordPost)
        if checkOld.activated == 0:
            returnDict['success'] = -3
            returnDict['message'] = 'Please activate your email'
            return HttpResponse(dumps(returnDict))
        returnDict['success'] = 1
        request.session['has_loggedin'] = True
        request.session['email'] = emailPost
        return HttpResponse(dumps(returnDict))
    except Person.DoesNotExist:
        returnDict['success'] = 0
        return HttpResponse(dumps(returnDict))


def checkIfLoggedIn(request):
    returnDict = {}
    returnDict['success'] = 0
    if request.session.get('has_loggedin',False):
        email = request.session.get('email',False)
        returnDict['success'] = email
        return HttpResponse(dumps(returnDict))
    else:
        return HttpResponse(dumps(returnDict))
