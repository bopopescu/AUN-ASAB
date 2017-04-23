# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('availability', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Facility',
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('facility', models.ForeignKey(to='reservation.Facility')),
            ],
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ('end_time',)},
        ),
        migrations.RenameField(
            model_name='holiday',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='venue',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='venue',
        ),
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(max_length=254, default=datetime.datetime(2017, 4, 12, 14, 30, 44, 470623, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='task_id',
            field=models.CharField(editable=False, max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='reservations_created'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected')], max_length=10, default='approved'),
        ),
        migrations.AddField(
            model_name='ownership',
            name='venue',
            field=models.ForeignKey(to='reservation.Venue'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='facility',
            field=models.ForeignKey(to='reservation.Facility', default=2, related_name='reservations'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='facilities',
            field=models.ManyToManyField(to='reservation.Facility', through='reservation.Ownership'),
        ),
    ]
