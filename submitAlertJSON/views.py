
from django.shortcuts import render
from registerJSON.models import Person
from submitAlertJSON.models import Alert
from json import dumps
# Create your views here.
from django.http import HttpResponse

def index(request):
    emailPost = request.POST.get("email")
    phonePost = request.POST.get("phone","")
    priceThresholdPost = request.POST.get("priceThreshold")
    signPost = request.POST.get("sign")
    emailOrTextPost = request.POST.get("emailOrText")    

    returnDict = {}
    person = Person.objects.get(email=emailPost)
    alertToAdd = Alert.objects.create(email=person)
    returnDict['success']=1
    return HttpResponse(dumps(returnDict))
