# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suplbizapp', '0003_auto_20160721_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='company_name',
            new_name='c_company_name',
        ),
        migrations.RenameField(
            model_name='provider',
            old_name='company_name',
            new_name='p_company_name',
        ),
    ]
