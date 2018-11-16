from django.db import models

# Create your models here.



class Blog(models.Model):
    b_name = models.CharField(max_length=32,verbose_name='日志标题')
    b_body = models.TextField(verbose_name='日志内容')
    b_time = models.DateTimeField(verbose_name='日志时间')
    b_to_t = models.ForeignKey(to="Title",on_delete=None)

    def __str__(self):
        return self.b_name

class Title(models.Model):
    t_name = models.CharField(max_length=32, verbose_name='文章类型')

    def __str__(self):
        return self.t_name