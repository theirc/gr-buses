# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buses_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsReceiver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('destination', models.PositiveIntegerField(blank=True, null=True, choices=[(1, 'Kara Tepe'), (2, 'Moria'), (3, 'Pikpa'), (4, 'Port')])),
                ('phone_number', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
    ]
