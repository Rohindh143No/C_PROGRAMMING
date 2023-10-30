from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def unit1(request):
    template=loader.get_template('unit1.html')
    return HttpResponse(template.render())
def unit2(request):
    template2=loader.get_template('unit2.html')
    return HttpResponse(template2.render())
def unit3(request):
    template3=loader.get_template('unit3.html')
    return HttpResponse(template3.render())


# Create your views here.
