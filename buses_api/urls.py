from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from django.conf.urls import include, url
from rest_framework import routers
from buses_api import  viewsets
from . import views

router = routers.SimpleRouter()
router.register('buses', viewsets.BusViewSet)

urlpatterns = [
                  url(r'^api/', include(router.urls, namespace='api')),
                  url(r'^import_from_kobo/', views.import_from_kobo),
              ]
