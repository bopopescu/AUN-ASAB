# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20170308_0536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holiday',
            name='title',
        ),
    ]
