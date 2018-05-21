# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id_city', models.AutoField(serialize=False, primary_key=True)),
                ('status', models.BooleanField(default=True)),
                ('city', models.CharField(max_length=45)),
                ('latitude', models.CharField(max_length=10, null=True, blank=True)),
                ('longitude', models.CharField(max_length=10, null=True, blank=True)),
                ('timezone', models.CharField(max_length=10, null=True, blank=True)),
                ('dmald', models.CharField(max_length=5, null=True, blank=True)),
                ('code', models.CharField(max_length=6, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id_country', models.AutoField(serialize=False, primary_key=True)),
                ('status', models.BooleanField(default=True)),
                ('country', models.CharField(max_length=45)),
                ('fips104', models.CharField(max_length=7)),
                ('iso2', models.CharField(max_length=4)),
                ('iso3', models.CharField(max_length=4)),
                ('ison', models.CharField(max_length=4)),
                ('internet', models.CharField(max_length=8)),
                ('capital', models.CharField(max_length=20)),
                ('map_ref', models.CharField(max_length=50)),
                ('nac_singular', models.CharField(max_length=30)),
                ('nac_plural', models.CharField(max_length=30)),
                ('currency', models.CharField(max_length=30)),
                ('currency_code', models.CharField(max_length=12)),
                ('population', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id_language', models.AutoField(serialize=False, primary_key=True)),
                ('status', models.BooleanField(default=True)),
                ('language', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=5, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id_state', models.AutoField(serialize=False, primary_key=True)),
                ('status', models.BooleanField(default=True)),
                ('state', models.CharField(max_length=45)),
                ('code', models.CharField(max_length=4)),
                ('adm1code', models.CharField(max_length=8)),
                ('country', models.ForeignKey(to='home.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(to='home.Country'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='home.State'),
            preserve_default=True,
        ),
    ]
