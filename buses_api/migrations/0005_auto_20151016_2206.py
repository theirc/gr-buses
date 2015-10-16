# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buses_api', '0004_smsreceiver_receive_case_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsreceiver',
            name='receive_case_information',
            field=models.BooleanField(default=True, verbose_name='Will this person receive case information?'),
        ),
    ]
