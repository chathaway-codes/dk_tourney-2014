from django.conf.urls import patterns, include, url

from tournament.views import TournamentListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tournaments/$', TournamentListView.as_view(), {}, 'tournament_list'),
)

