"""crontab_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from cmanage import views

urlpatterns = [
    url(r'^login/$', views.my_login, name="login"),
    url(r'^logout/$', views.my_logout, name='logout'),
    url(r'^home/$', views.home, name="home"),
    url(r'^hosts/$', views.hosts, name="hosts"),
    url(r'^host/add/$', views.host_add, name="host_add"),
    url(r'^host/del/$', views.host_del, name="host_del"),
    url(r'^host/(?P<host_id>\d+)/info/$', views.host_info, name="host_info"),
    url(r'^hosts/(?P<host_id>\d+)/tasks/$', views.hosts_task, name="hosts_task"),
    url(r'^host_groups/$', views.host_groups, name="host_groups"),
    url(r'^records/$', views.records, name="records"),
]
