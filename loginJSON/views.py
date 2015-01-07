from django.shortcuts import render
from registerJSON.models import Person
from django.http import HttpResponse
from json import dumps
# Create your views here.

def index(request):
    emailPost = request.POST.get("email", "")
    passwordPost = request.POST.get("password", "")
    returnDict = {}
    
    try:
        checkOld = Person.objects.get(email=emailPost, password=passwordPost)
        returnDict['success'] = 1
        return HttpResponse(dumps(returnDict))
    except Person.DoesNotExist:
        returnDict['success'] = 0
        return HttpResponse(dumps(returnDict))
