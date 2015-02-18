__author__ = 'Om Tripathi'
from django.conf.urls import url, patterns, include
from sms_cbv import views

urlpatterns = patterns('',
                       url(r'^$', views.UserLogin.as_view()),
                       url(r'^register/$', views.UserRegistration.as_view()),
                       (r'^accounts/', include('registration.backends.default.urls')),

)
