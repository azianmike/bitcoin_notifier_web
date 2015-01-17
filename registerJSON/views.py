from django.shortcuts import render
from registerJSON.models import Person
from json import dumps
import datetime
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
        userToAdd = Person.objects.create(email=emailPost, password=passwordPost,joinDate=mysqlTime)    
        userToAdd.phone = phonePost
        userToAdd.save()
        returnDict['success']=1
        return HttpResponse(dumps(returnDict))
