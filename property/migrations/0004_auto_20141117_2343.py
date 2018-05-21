# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20141117_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='zip_code',
            field=models.IntegerField(default=0, max_length=5, null=True, blank=True),
        ),
    ]
