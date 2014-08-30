# Talk urls
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'talk.views',
    url(r'^$', 'home'),
    url(r'^create_post/$', 'create_post'),
    url(r'^delete_post/$', 'delete_post'),
)
