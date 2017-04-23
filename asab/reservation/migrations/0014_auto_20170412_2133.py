# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0013_venue_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
