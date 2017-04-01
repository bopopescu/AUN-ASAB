# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_remove_reservation_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='venue',
            field=models.ForeignKey(to='reservation.Venue', default=1, related_name='reservations'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='reservations_created'),
        ),
    ]
