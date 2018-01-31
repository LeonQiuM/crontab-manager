#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Leon"
# Date: 2018/1/30


from django import template
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def build_path_ele(path1, path2, path3):
    """
    <li><a href="#">{{ path1 }}</a></li>所在路径
    :param path1:
    :param path2:
    :param path3:
    :return:
    """
    path_ele = a_tag = ""
    map_path = {
        "users": '用户',
        "hosts": '主机',
        "host_groups": '主机组',
        "records": '任务'
    }
    for k, v in map_path.items():
        if path2 == v:
            a_tag = reverse(k, kwargs={})
    path_ele += '<li>%s</li>' % path1
    path_ele += '<li class="active"><a href="%s">%s</a></li>' % (a_tag, path2)
    if path3:
        path_ele += '<li class="active">%s</li>' % path3
    return mark_safe(path_ele)


@register.simple_tag
def build_rule_ele(rules_obj):
    td_ele = ""
    for rule in rules_obj:
        record = "%s  %s  %s  %s  %s  %s" % (rule.minute, rule.hour, rule.day, rule.month, rule.week, rule.command)
        td_ele += """<table class='table-bordered'><tr><td>%s</td></tr></table>""" % record

    return mark_safe(td_ele)
