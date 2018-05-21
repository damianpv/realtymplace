# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('email', models.CharField(max_length=45, blank=True)),
                ('phone', models.CharField(max_length=45, blank=True)),
                ('agency', models.CharField(max_length=100, blank=True)),
                ('how_know_us', models.CharField(max_length=100, blank=True)),
                ('subject', models.CharField(max_length=45, blank=True)),
                ('message', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(to='home.Country', null=True)),
                ('language', models.ForeignKey(to='home.Language', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
