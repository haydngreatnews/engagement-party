from django.conf.urls import patterns, url

from rsvp import views

urlpatterns = patterns('',
    # ex: /rsvp/
    url(r'^$', views.index, name='index'),
    # ex: /rsvp/5/
    url(r'^(?P<invite_id>\d+)/$', views.respond, name='respond'),
    # ex: /rsvp/search/?q=Tom
    url(r'^search.json\?(?P<query>.*)$', views.search, name='search'),
)
