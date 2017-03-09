# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_holiday_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]
