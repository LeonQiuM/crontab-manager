from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from cmanage import models
from cmanage import serializers
from rest_framework import permissions


class HostViewSet(viewsets.ModelViewSet):
    queryset = models.Host.objects.all()
    serializer_class = serializers.HostSerializers
    permission_classes = (permissions.IsAuthenticated,)


class HostGroupViewSet(viewsets.ModelViewSet):
    queryset = models.HostGroup.objects.all()
    serializer_class = serializers.HostGroupSerializers
    permission_classes = (permissions.IsAuthenticated,)


class RuleRecordViewSet(viewsets.ModelViewSet):
    queryset = models.RuleRecord.objects.all()
    serializer_class = serializers.RuleRecordSerializers
    permission_classes = (permissions.IsAuthenticated,)
