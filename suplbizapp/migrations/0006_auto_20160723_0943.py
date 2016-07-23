# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suplbizapp', '0005_auto_20160723_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='provider_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
