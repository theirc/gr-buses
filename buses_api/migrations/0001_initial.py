# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusTripInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kobo_id', models.CharField(max_length=60, null=True, verbose_name='Kobo Instance Id', blank=True)),
                ('kobo_data', models.TextField(null=True, verbose_name='Kobo Submitted Data', blank=True)),
                ('estimated_time_arrival', models.DateTimeField(auto_now_add=True, verbose_name='Estimated Time Of Arrival', null=True)),
                ('actual_time_arrival', models.DateTimeField(null=True, verbose_name='Estimated Time Of Arrival', blank=True)),
            ],
        ),
    ]
