from django.shortcuts import render
from registerJSON.models import Person
# Create your views here.
from django.http import HttpResponse

def index(request):
    emailPost = request.POST.get("email", "")
    phonePost = request.POST.get("phone")
    passwordPost = request.POST.get("password", "")
    try:
        checkOld = Person.objects.get(email=emailPost)
        return HttpResponse('email already exists')
    except Person.DoesNotExist:
        userToAdd = Person.objects.create(email=emailPost, password=passwordPost)    
        userToAdd.phone = phonePost
        userToAdd.save()
        return HttpResponse('success')
