# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suplbizapp', '0002_auto_20160721_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='region',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='region',
        ),
        migrations.AddField(
            model_name='client',
            name='regions',
            field=models.ManyToManyField(to='suplbizapp.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='regions',
            field=models.ManyToManyField(to='suplbizapp.Region'),
            preserve_default=True,
        ),
    ]
