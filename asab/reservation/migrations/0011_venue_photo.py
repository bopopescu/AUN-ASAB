# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0010_remove_reservation_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='photo',
            field=models.ImageField(blank=True, upload_to='venues/%Y/%m/%d'),
        ),
    ]
