__author__ = 'Om Tripathi'

from django.conf.urls import url, patterns

from sms_cbv import views


urlpatterns = patterns('',
                       url(r'^$', views.UserLogin.as_view()),
                       #url(r'^sms/$', views.user_login)
)
