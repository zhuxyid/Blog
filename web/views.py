from django.shortcuts import render
from web import models
# Create your views here.


def index(request):
    title = models.Title.objects.all()
    blog = models.Blog.objects.all()
    return render(request,"index.html",locals())
