# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_remove_venue_facilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='facilities',
            field=models.ManyToManyField(to='reservation.Facility', through='reservation.Ownership'),
        ),
    ]
