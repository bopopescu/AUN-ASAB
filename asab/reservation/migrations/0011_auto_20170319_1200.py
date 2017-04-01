# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0010_auto_20170318_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(max_length=10, choices=[('approved', 'Approved'), ('rejected', 'Rejected')], default='approved'),
        ),
    ]
