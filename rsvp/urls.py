from django.conf.urls import patterns, url

from rsvp import views

urlpatterns = patterns('',
    # ex: /rsvp/
    url(r'^$', views.index, name='index'),
    # ex: /rsvp/5/
    # url(r'^(?P<pk>\d+)/$', views.InviteReturnView.as_view(), name='invite_return'),
    # ex: /rsvp/<md5sum>/
    url(r'^(?P<slug>[0-9a-z]+)/$', views.InviteReturnView.as_view(), name='invite_return'),
    # ex: /rsvp/search.json?q=Tom
    url(r'^search.json$', views.search, name='search'),
    # ex: /rsvp/thanks/
    url(r'^thanks', views.thanks, name='thanks'),
)
