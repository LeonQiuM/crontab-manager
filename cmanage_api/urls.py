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
from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from cmanage_api import views

schema_view = get_schema_view(title="定时任务管理")
router = DefaultRouter()
router.register(r'host', views.HostViewSet, )
router.register(r'host_group', views.HostGroupViewSet, )
router.register(r'role_record', views.RuleRecordViewSet, )

obtain_expiring_auth_token = views.ObtainExpiringAuthToken.as_view()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/', schema_view),
    url(r'^docs/', include_docs_urls(title="任务管理API文档")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth/', obtain_expiring_auth_token, name="api-token"),
]
