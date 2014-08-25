from django.conf.urls import patterns, include, url
from talk_project.views import logout_page

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    url(r'^', include('talk.urls')),
)
