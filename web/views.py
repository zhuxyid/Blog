from django.shortcuts import render
from django.http import JsonResponse
from web import models
# Create your views here.



def index(request):
    info = models.Information.objects.all()
    return render(request,"index.html",locals())

def get_img(request):
    nid = request.GET.get('nid')
    img_list = models.Img.objects.values('id','src','title')
    img_list = list(img_list)
    ret = {
        'status':True,
        'DATA':img_list
    }
    return JsonResponse(ret)