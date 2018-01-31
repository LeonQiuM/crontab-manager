from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from cmanage import models
from cmanage_api import serializers
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
import datetime
from django.utils.timezone import utc
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response


class ObtainExpiringAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])
            utc_now = datetime.datetime.utcnow().replace(tzinfo=utc)
            EXPIRE_MINUTES = getattr(settings, 'REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES', 1)
            if created or token.created < utc_now - datetime.timedelta(minutes=EXPIRE_MINUTES):
                token.delete()
                token = Token.objects.create(user=serializer.validated_data['user'])
                token.created = utc_now
                token.save()
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class HostRuleStatusViewSet(viewsets.ModelViewSet):
    queryset = models.HostRuleStatus.objects.all()
    serializer_class = serializers.HostRuleStatusSerializers
    permission_classes = (permissions.IsAuthenticated,)