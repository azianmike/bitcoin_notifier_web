from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    if request.session.get('has_loggedin',False):
        email = request.session.get('email',False)
        return HttpResponse(email)
    else:
        return HttpResponse('not logged in')
