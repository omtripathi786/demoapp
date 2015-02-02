__author__ = 'Om Tripathi'

from django.conf.urls import url, patterns

from sms import views


urlpatterns = patterns('',
                       url(r'^$', views.user_login, name='user_login'),
                       url(r'^logout/$', views.user_logout, name='user_logout'),
                       url(r'^sms/$', views.index, name='index'),
                       url(r'^sms/register/$', views.register, name='register')
)
