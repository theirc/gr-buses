from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from django.http import HttpResponse
from django.conf import settings
import requests
from . import models
import ujson as json
from twilio.rest import TwilioRestClient
import dateutil.parser
from datetime import timedelta


def import_from_kobo(request):
    kobo_url = getattr(settings, "KOBO_BASE_URL", "https://kc.humanitarianresponse.info/api/v1/data/")
    kobo_form_id = getattr(settings, "KOBO_FORM_ID", 27848)
    kobo_username = getattr(settings, "KOBO_USERNAME", "")
    kobo_password = getattr(settings, "KOBO_PASSWORD", "")

    twilio = TwilioRestClient(account=settings.TWILIO_ACCOUNT_SID, token=settings.TWILIO_AUTH_TOKEN)

    print("Requesting {}{}".format(kobo_url, kobo_form_id))

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

    destination_friendly = {
        1: "Kara Tepe",
        2: "Moria",
        3: "Pikpa",
        4: "the Port",
    }

    for d in data:
        exists = models.BusTripInstance.objects.filter(kobo_id=d['_uuid']).count()
        if not exists:
            models.BusTripInstance.objects.create(kobo_id=d['_uuid'], kobo_data=text)
            destinations = [destination_dictionary[c] for c in d['Destination'].split(' ')]
            sent_on = dateutil.parser.parse(d['_submission_time'])
            sent_on = sent_on + timedelta(hours=2)

            for c in models.SmsReceiver.objects.filter(destination__in=destinations, enabled=True):
                twilio.messages.create(from_="IRC", to=c.phone_number,
                                       body="A bus has been dispatched to {} at {}."
                                       .format(destination_friendly[c.destination], sent_on.strftime("%H:%M:%S")))

                if d['Are_there_any_vulnerable_cases'] == 'yes' and c.receive_case_information:
                    twilio.messages.create(from_="IRC", to=c.phone_number,
                                           body=d['vulnerable_case_description'])
    return HttpResponse('')
