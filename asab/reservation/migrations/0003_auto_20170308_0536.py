# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20170308_0525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='holiday',
            old_name='name',
            new_name='title',
        ),
    ]
