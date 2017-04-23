# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_remove_venue_facilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='facilities',
            field=models.ManyToManyField(through='reservation.Ownership', to='reservation.Facility'),
        ),
    ]
