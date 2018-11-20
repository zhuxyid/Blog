from django.shortcuts import render
from web import models
# Create your views here.


def index(request):
    return render(request,"index.html",locals())
