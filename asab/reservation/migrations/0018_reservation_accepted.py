# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0017_remove_reservation_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='accepted',
            field=models.BooleanField(default=True),
        ),
    ]
