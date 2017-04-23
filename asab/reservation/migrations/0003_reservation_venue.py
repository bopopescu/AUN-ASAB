# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20170412_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='venue',
            field=models.ForeignKey(to='reservation.Venue', default=3),
            preserve_default=False,
        ),
    ]
