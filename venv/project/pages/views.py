from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse('Hello From Index')

def about(response):
    return HttpResponse('Hello From About')