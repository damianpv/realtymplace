# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0008_auto_20141215_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='zip_code',
            field=models.IntegerField(null=True),
        ),
    ]
