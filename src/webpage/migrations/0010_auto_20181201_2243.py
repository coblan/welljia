# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-01 22:43
from __future__ import unicode_literals

from django.db import migrations, models
import helpers.director.model_func.cus_fields.cus_picture


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0009_area_mainpageitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='pic',
            field=helpers.director.model_func.cus_fields.cus_picture.PictureField(blank=True, max_length=300, verbose_name='区域图'),
        ),
        migrations.AlterField(
            model_name='mainpageitem',
            name='area',
            field=models.ManyToManyField(blank=True, to='webpage.Area', verbose_name='区域'),
        ),
        migrations.AlterField(
            model_name='mainpageitem',
            name='project',
            field=models.ManyToManyField(blank=True, to='webpage.MapPoint', verbose_name='项目点'),
        ),
    ]
