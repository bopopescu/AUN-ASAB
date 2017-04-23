# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0011_venue_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
