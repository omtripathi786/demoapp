__author__ = 'Om Tripathi'

from django.conf.urls import url, patterns, include

from sms import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
                       url(r'^$', views.user_login, name='user_login'),
                       url(r'^logout/$', views.user_logout, name='user_logout'),
                       url(r'^sms/$', views.index, name='index'),
                       url(r'^sms/register/$', views.register, name='register'),
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
