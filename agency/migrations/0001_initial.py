# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to=b'logo')),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('about_us', models.TextField()),
                ('email', models.EmailField(max_length=75)),
                ('url_slug', models.SlugField(max_length=200, error_messages={b'unique': b'Ya existe'})),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(to='home.Country')),
                ('language', models.ForeignKey(to='home.Language')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
