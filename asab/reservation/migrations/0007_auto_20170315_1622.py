# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_venue_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='venue',
            field=models.ForeignKey(related_name='reservations', to='reservation.Venue'),
        ),
    ]
