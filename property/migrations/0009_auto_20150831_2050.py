# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20150316_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='feature',
            field=models.ManyToManyField(to='property.Feature'),
        ),
    ]
