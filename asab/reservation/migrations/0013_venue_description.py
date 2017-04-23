# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0012_venue_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='description',
            field=models.TextField(default=datetime.datetime(2017, 4, 12, 20, 32, 25, 751808, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
