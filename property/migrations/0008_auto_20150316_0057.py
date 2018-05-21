# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20141230_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='city',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
