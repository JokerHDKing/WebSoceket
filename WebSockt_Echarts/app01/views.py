from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from app01.models import User


# Create your views here.
def index(request):
    return  render(request,'bar-brush.html')