# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0005_auto_20141123_2358'),
        ('property', '0005_auto_20141117_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic',
            name='agency',
            field=models.ForeignKey(related_name=b'property_agency', default=None, to='agency.Agency'),
            preserve_default=False,
        ),
    ]
