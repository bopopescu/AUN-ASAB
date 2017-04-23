# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0016_reservation_venue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='venue',
        ),
    ]
