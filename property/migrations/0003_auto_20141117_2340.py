# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_remove_basic_admin_comments1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='zip_code',
            field=models.IntegerField(max_length=5, null=True, blank=True),
        ),
    ]
