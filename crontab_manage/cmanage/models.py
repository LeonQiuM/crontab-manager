from django.db import models


# Create your models here.


class HostGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=32, unique=True, null=False)

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name_plural = verbose_name = "主机组"


class Host(models.Model):
    host_id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=64)
    host_ip = models.GenericIPAddressField()
    groups = models.ManyToManyField('HostGroup')
    rules = models.ManyToManyField('RuleRecord')

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name_plural = verbose_name = "主机"
        unique_together = (('hostname', "host_ip"),)


class RuleRecord(models.Model):
    minute = models.CharField(max_length=12)
    hour = models.CharField(max_length=12)
    day = models.CharField(max_length=12)
    month = models.CharField(max_length=12)
    week = models.CharField(max_length=12)
    command = models.CharField(max_length=128)
