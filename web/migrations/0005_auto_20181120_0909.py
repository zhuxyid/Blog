# Generated by Django 2.1.3 on 2018-11-20 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20181120_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='img',
            field=models.ImageField(null=True, upload_to='static/img/', verbose_name='头像'),
        ),
    ]