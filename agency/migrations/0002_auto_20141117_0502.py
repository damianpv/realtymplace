# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agency', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agency',
            old_name='url_slug',
            new_name='slug',
        ),
        migrations.AddField(
            model_name='agency',
            name='user',
            field=models.ForeignKey(related_name=b'agency_user', default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agency',
            name='visit',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
