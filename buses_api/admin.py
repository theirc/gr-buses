from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from django.contrib import admin

from .models import BusTripInstance, SmsReceiver, DriverInformation, PurchaseRequestInformation, BusInformation

admin.site.register(BusTripInstance)
admin.site.register(SmsReceiver)

"""
admin.site.register(DriverInformation)
admin.site.register(PurchaseRequestInformation)
admin.site.register(BusInformation)
"""