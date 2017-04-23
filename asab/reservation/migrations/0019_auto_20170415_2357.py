# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0018_reservation_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='level',
            field=models.CharField(default='FRESHMAN', choices=[('Freshman', 'FRESHMAN'), ('Sophmore', 'SOPHMORE'), ('Junior', 'JUNIOR'), ('Senior', 'SENIOR')], max_length=25),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reason',
            field=models.TextField(null=True, blank=True),
        ),
    ]
