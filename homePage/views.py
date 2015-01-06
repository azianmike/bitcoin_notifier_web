from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render_to_response('index.html')  
