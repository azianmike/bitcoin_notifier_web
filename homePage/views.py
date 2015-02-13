from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.shortcuts import render_to_response, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.
from django.http import HttpResponse

@ensure_csrf_cookie
def index(request):
    if request.session.get('has_loggedin',False):
        url = reverse('loginHome', args=(),kwargs={})
        return HttpResponseRedirect(url)
    else:
        request.session['store_cookie'] = True
        return render(request,'index.html')
        #return render(request,'index.html', {'test':'<body onload=\"javascript:showAlertMessage(&quot;test&quot;);\">'})  

@ensure_csrf_cookie
def loginHome(request):
    if request.session.get('has_loggedin',False):

        return render(request, 'loginHome.html')
    else:
        return HttpResponse("Please login first")
