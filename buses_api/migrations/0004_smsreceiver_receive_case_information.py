# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buses_api', '0003_businformation_driverinformation_purchaserequestinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='smsreceiver',
            name='receive_case_information',
            field=models.NullBooleanField(verbose_name='Will this person receive case information?'),
        ),
    ]
