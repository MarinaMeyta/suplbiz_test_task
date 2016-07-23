# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suplbizapp', '0004_auto_20160722_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='regions',
            new_name='c_regions',
        ),
        migrations.RenameField(
            model_name='provider',
            old_name='regions',
            new_name='p_regions',
        ),
    ]
