from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

import keplerapp_tbcheck
from keplerapp_tbcheck import urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'keplerweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^demo/', include(keplerapp_tbcheck.urls)),
    url(r'^$', include(keplerapp_tbcheck.urls)),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', include(admin.site.urls))
)
