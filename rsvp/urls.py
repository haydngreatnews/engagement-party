from django.conf.urls import patterns, url

from rsvp import views

urlpatterns = patterns('',
    # ex: /rsvp/
    url(r'^$', views.index, name='index'),
    # ex: /rsvp/5/
    url(r'^(?P<pk>\d+)/$', views.InviteReturnView.as_view(), name='invite_return'),
    # ex: /rsvp/search.json?q=Tom
    url(r'^search.json$', views.search, name='search'),
)
