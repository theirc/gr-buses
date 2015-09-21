from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from django.http import HttpResponse
from django.conf import settings
import requests
from . import models
import ujson as json
from twilio.rest import TwilioRestClient


def import_from_kobo(request):
    kobo_url = getattr(settings, "KOBO_BASE_URL", "https://kc.humanitarianresponse.info/api/v1/data/")
    kobo_form_id = getattr(settings, "KOBO_FORM_ID", 27848)
    kobo_username = getattr(settings, "KOBO_USERNAME", "")
    kobo_password = getattr(settings, "KOBO_PASSWORD", "")

    twilio = TwilioRestClient(account=settings.TWILIO_ACCOUNT_SID, token=settings.TWILIO_AUTH_TOKEN)

    print ("Requesting {}{}".format(kobo_url, kobo_form_id))

    request = requests.get("{}{}".format(kobo_url, kobo_form_id), headers={"Accept": "application/json"},
                           auth=(kobo_username, kobo_password))

    text = request.text
    data = json.loads(text)
    destination_dictionary = {
        "kara_tepe": 1,
        "moria": 2,
        "pikpa": 3,
        "port_mytilini": 4
    }

    for d in data:
        exists = models.BusTripInstance.objects.filter(kobo_id=d['_uuid']).count()
        if not exists:
            models.BusTripInstance.objects.create(kobo_id=d['_uuid'], kobo_data=text)
            destinations = [destination_dictionary[c] for c in d['Destination'].split(' ')]

            for c in models.SmsReceiver.objects.filter(destination__in=destinations):
                twilio.messages.create(from_="IRC", to=c.phone_number,
                                       body="A bus has been dispatched to your location.")
    return HttpResponse('')