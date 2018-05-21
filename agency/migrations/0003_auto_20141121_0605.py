# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('agency', '0002_auto_20141117_0502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='about_us',
        ),
        migrations.AddField(
            model_name='agency',
            name='city',
            field=models.CharField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agency',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agency',
            name='state',
            field=models.ForeignKey(default=None, to='home.State'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agency',
            name='zip_code',
            field=models.IntegerField(max_length=5, null=True),
            preserve_default=True,
        ),
    ]
