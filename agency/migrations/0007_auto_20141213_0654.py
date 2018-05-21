# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('agency', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('email', models.CharField(max_length=45, blank=True)),
                ('subject', models.CharField(max_length=45, blank=True)),
                ('message', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agency', models.ForeignKey(to='agency.Agency')),
                ('country', models.ForeignKey(related_name=b'contact_country', to='home.Country', null=True)),
                ('language', models.ForeignKey(related_name=b'contact_language', to='home.Language', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='contact',
            name='agency',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='country',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='language',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
