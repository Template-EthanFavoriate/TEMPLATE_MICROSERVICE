from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'', 'keplerapp_tbcheck.views.service_check'),
    url(r'template', 'keplerapp_tbcheck.views.service_default')
)
