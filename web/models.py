from django.db import models

# Create your models here.

class Information(models.Model):
    email = models.CharField(max_length=32,verbose_name='邮箱',null=True)
    motto = models.CharField(max_length=64,verbose_name='签名',null=True)
    summary = models.TextField(verbose_name='概述',null=True)
    gitlink = models.URLField(verbose_name='GIT链接',null=True)
    wblink = models.URLField(verbose_name='WEIBO链接',null=True)
    inslink = models.URLField(verbose_name='INS链接',null=True)
    img = models.ImageField(verbose_name='头像',null=True,upload_to='static/img/')
    wximg = models.ImageField(verbose_name='微信公众号头像',null=True,upload_to='static/img/wx/')
    def __str__(self):
        return '个人设置'