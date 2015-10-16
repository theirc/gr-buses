from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from django.db import models
from django.utils.translation import ugettext as _

DESTINATION_CHOICES = (
    (1, 'Kara Tepe'),
    (2, 'Moria'),
    (3, 'Pikpa'),
    (4, 'Port'),
)


class BusTripInstance(models.Model):
    kobo_id = models.CharField(max_length=60, null=True, blank=True, verbose_name=_("Kobo Instance Id"))
    kobo_data = models.TextField(null=True, blank=True, verbose_name=_("Kobo Submitted Data"))
    estimated_time_arrival = models.DateTimeField(null=True, auto_now_add=True,
                                                  verbose_name=_("Estimated Time Of Arrival"))
    actual_time_arrival = models.DateTimeField(null=True, blank=True, verbose_name=_("Estimated Time Of Arrival"))


class SmsReceiver(models.Model):
    destination = models.PositiveIntegerField(blank=True, null=True, choices=DESTINATION_CHOICES)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    receive_case_information = models.BooleanField(default=True,
                                                   verbose_name=_('Will this person receive case information?'))


class DriverInformation(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, )


class BusInformation(models.Model):
    license_plate = models.CharField(max_length=100, null=True, blank=True, )


class PurchaseRequestInformation(models.Model):
    identifier = models.CharField(max_length=100, null=True, blank=True, )