from django.shortcuts import render

from django.core.context_processors import csrf

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'index.html', {})