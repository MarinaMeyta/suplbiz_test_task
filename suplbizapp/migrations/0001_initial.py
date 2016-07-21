# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('company_name', models.TextField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('provider_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('company_name', models.TextField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('region_name', models.TextField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='provider',
            name='regions',
            field=models.ForeignKey(to='suplbizapp.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='regions',
            field=models.ForeignKey(to='suplbizapp.Region'),
            preserve_default=True,
        ),
    ]
