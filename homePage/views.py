from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.
from django.http import HttpResponse

@ensure_csrf_cookie
def index(request):
    return render_to_response('index.html')  

@ensure_csrf_cookie
def loginHome(request):
    return render_to_response('loginHome.html')
