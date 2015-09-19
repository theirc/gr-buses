from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from rest_framework import viewsets, serializers
from . import models
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BusTripInstance


class BusViewSet(viewsets.ModelViewSet):
    queryset = models.BusTripInstance.objects.all()
    serializer_class = BusSerializer
