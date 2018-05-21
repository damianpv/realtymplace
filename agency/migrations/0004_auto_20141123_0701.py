# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_auto_20141121_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='cell',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agency',
            name='phone',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agency',
            name='website',
            field=models.URLField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
