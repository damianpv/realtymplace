# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0006_basic_agency'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'property', blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('basic', models.ForeignKey(to='property.Basic')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='basic',
            name='zip_code',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
