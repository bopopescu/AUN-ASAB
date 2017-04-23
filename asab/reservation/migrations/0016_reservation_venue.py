# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0015_venue_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='venue',
            field=models.ForeignKey(null=True, to='reservation.Venue'),
        ),
    ]
