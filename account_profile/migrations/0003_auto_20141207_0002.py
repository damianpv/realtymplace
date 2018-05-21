# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Perfil de Usuario', 'verbose_name_plural': 'Perfiles de Usuarios'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='about_me',
            field=models.TextField(null=True, blank=True),
        ),
    ]
