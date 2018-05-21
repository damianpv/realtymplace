# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20141117_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='zip_code',
            field=models.IntegerField(max_length=5, null=True),
        ),
    ]
