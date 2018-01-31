#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Leon"
# Date: 2018/1/25


from cmanage import models
from rest_framework import serializers


class HostSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Host
        fields = ('host_id', 'hostname', 'host_ip', 'groups',)


class HostGroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.HostGroup
        fields = ('group_id', 'group_name')


class RuleRecordSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RuleRecord
        fields = ('id', 'minute', 'hour', 'day', 'month', 'week', 'command')


class HostRuleStatusSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.HostRuleStatus
        fields = ('id', 'enable', 'host', 'rule')
