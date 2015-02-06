__author__ = 'Om Tripathi'

from django.conf.urls import url, patterns

from sms_cbv import views


urlpatterns = patterns('',
        url(r'^$', views.user_login, name='user_login')
)
