# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True)),
                ('address', models.CharField(max_length=255, blank=True)),
                ('city', models.CharField(max_length=15, blank=True)),
                ('zip_code', models.IntegerField(max_length=5, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('bedroom', models.PositiveIntegerField(default=0)),
                ('bathroom', models.PositiveIntegerField(default=0)),
                ('area', models.PositiveIntegerField(default=0)),
                ('garage', models.PositiveIntegerField(default=0)),
                ('allow_rating', models.BooleanField(default=0)),
                ('admin_comments', models.TextField(blank=True)),
                ('admin_comments1', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, error_messages={b'unique': b'Ya existe.'})),
                ('visit', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(related_name=b'property_country', to='home.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
                ('order', models.PositiveIntegerField()),
                ('url_slug', models.SlugField(blank=True, max_length=200, null=True, error_messages={b'unique': b'Ya existe.'})),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=20)),
                ('order', models.PositiveIntegerField()),
                ('url_slug', models.SlugField(blank=True, max_length=200, null=True, error_messages={b'unique': b'Ya existe.'})),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=20)),
                ('order', models.PositiveIntegerField()),
                ('url_slug', models.SlugField(blank=True, max_length=200, null=True, error_messages={b'unique': b'Ya existe.'})),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='basic',
            name='feature',
            field=models.ManyToManyField(to='property.Feature', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basic',
            name='language',
            field=models.ForeignKey(related_name=b'property_language', to='home.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basic',
            name='state',
            field=models.ForeignKey(related_name=b'property_state', to='home.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basic',
            name='status',
            field=models.ForeignKey(to='property.Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basic',
            name='type',
            field=models.ForeignKey(to='property.Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basic',
            name='user',
            field=models.ForeignKey(related_name=b'property_user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
