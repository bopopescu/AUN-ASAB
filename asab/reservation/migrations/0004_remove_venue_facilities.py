# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_reservation_venue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='facilities',
        ),
    ]
