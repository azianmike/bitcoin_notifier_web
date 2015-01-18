from django.shortcuts import render
#from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def index(request):
    #return render(request, 'login.html',{})
    #
    request.session.flush()
    return redirect('/')
