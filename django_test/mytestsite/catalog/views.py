from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)
# Create your views here.
from .models import Coffee
from django.http import HttpResponse, HttpResponseNotFound
def home(request):
    print('进入 home 视图')
    template='home.html'
    return render(request, template)
def menu(request):
    print('进入 menu 视图')
    coffee   = Coffee.objects.all()
    template = 'menu.html'
    return render(request, template, {'coffee':coffee})
# def other(request):
#     print('进入 other 视图')
#     template='other.html'
#     return render(request, template)
def other(request):
    print("request = "+str(request))
    _url = request.path
    print("_url = "+str(_url))
    return HttpResponse(f"The requested URL '{_url}' was not found.")
    # return HttpResponseNotFound('Page not found')