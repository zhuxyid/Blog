from django.shortcuts import render,render_to_response
from web import models
# Create your views here.


def index(request):
    info = models.Information.objects.all()
    return render(request,"index.html",locals())
