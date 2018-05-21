# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0004_auto_20141123_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='agency',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'logo', blank=True),
        ),
        migrations.AlterField(
            model_name='agency',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
