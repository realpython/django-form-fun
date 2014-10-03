# Talk urls
from django.conf.urls import patterns, url
from talk import views


urlpatterns = patterns(
    'talk.views',
    url(r'^$', 'home'),

    # api
    url(r'^api/v1/posts/$', views.PostCollection.as_view()),
    url(r'^api/v1/posts/(?P<pk>[0-9]+)/$', views.PostMember.as_view())
)
