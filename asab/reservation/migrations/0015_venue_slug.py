# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0014_auto_20170412_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2017, 4, 13, 20, 3, 18, 642311, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
