from django.db import models


# Create your models here.


class HostGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=32, unique=True, null=False, verbose_name="组名")

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name_plural = verbose_name = "主机组"
        ordering = ('group_id',)


class Host(models.Model):
    host_id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=64, verbose_name="主机名")
    host_ip = models.GenericIPAddressField(verbose_name='内网IP地址')
    groups = models.ManyToManyField('HostGroup')

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name_plural = verbose_name = "主机"
        unique_together = (('hostname', "host_ip"),)
        ordering = ('host_id',)


class HostRuleStatus(models.Model):
    enable = models.BooleanField()
    host = models.ForeignKey(to='Host', to_field='host_id')
    rule = models.ForeignKey('RuleRecord')

    class Meta:
        verbose_name_plural = verbose_name = "主机任务状态"
        unique_together = (('host', "rule"),)
        ordering = ('id',)


class RuleRecord(models.Model):
    minute = models.CharField(max_length=12, verbose_name="分")
    hour = models.CharField(max_length=12, verbose_name="时")
    day = models.CharField(max_length=12, verbose_name="日")
    month = models.CharField(max_length=12, verbose_name="月")
    week = models.CharField(max_length=12, verbose_name="周")
    command = models.CharField(max_length=128, verbose_name="命令")

    def __str__(self):
        return "%s  %s  %s  %s  %s  %s" % (
            self.minute,
            self.hour,
            self.day,
            self.month,
            self.week,
            self.command
        )

    class Meta:
        verbose_name_plural = verbose_name = "任务"
        ordering = ('id',)
