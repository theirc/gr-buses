from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from django.contrib import admin

from .models import BusTripInstance, SmsReceiver, DriverInformation, PurchaseRequestInformation, BusInformation


class SmsReceiverAdmin(admin.ModelAdmin):
    list_display = ('destination', 'phone_number', 'receive_case_information')

admin.site.register(BusTripInstance)
admin.site.register(SmsReceiver,SmsReceiverAdmin)

"""
admin.site.register(DriverInformation)
admin.site.register(PurchaseRequestInformation)
admin.site.register(BusInformation)
"""