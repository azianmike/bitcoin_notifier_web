from django.shortcuts import render
from registerJSON.models import Person
# Create your views here.
from django.http import HttpResponse

def index(request):
    try:
        checkOld = Person.objects.get(email='test@test.com')
        return HttpResponse('email already exists')
    except Person.DoesNotExist:
        test = Person.objects.create(email='test@test.com', password='test')    
        test.email = 'test@test.com'
        test.password = 'hashed pass'
        test.save()
        return HttpResponse('finished testing')
