from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('sms.urls')),
    url(r'^sms/', include('sms.urls')),
    url(r'^sms_cbv/', include('sms_cbv.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
