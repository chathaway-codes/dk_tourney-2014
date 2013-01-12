from django.conf.urls import patterns, include, url

from tournament.views import TournamentListView, GameListView, GameDetailView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tournaments/$', TournamentListView.as_view(), {}, 'tournament_list'),
    url(r'^games/$', GameListView.as_view(), {}, 'game_list'),

    url(r'^games/(?P<pk>\d+)/$', GameDetailView.as_view(), {}, 'game_detail'),
)

