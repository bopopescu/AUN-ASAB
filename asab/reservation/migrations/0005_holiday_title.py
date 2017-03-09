# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_remove_holiday_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='holiday',
            name='title',
            field=models.CharField(max_length=150, default=datetime.datetime(2017, 3, 8, 13, 44, 55, 559959, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
