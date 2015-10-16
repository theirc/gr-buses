# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buses_api', '0005_auto_20151016_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='smsreceiver',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
