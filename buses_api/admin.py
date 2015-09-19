from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from django.contrib import admin

from .models import BusTripInstance, SmsReceiver

admin.site.register(BusTripInstance)
admin.site.register(SmsReceiver)
