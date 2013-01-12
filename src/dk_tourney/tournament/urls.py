from django.conf.urls import patterns, include, url

from tournament.views import TournamentListView, TournamentDetailView, GameListView, GameDetailView, PlayerListView, PlayerDetailView, interest_in_game

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tournaments/$', TournamentListView.as_view(), {}, 'tournament_list'),
    url(r'^games/$', GameListView.as_view(), {}, 'game_list'),

    url(r'^tournaments/(?P<pk>\d+)/$', TournamentDetailView.as_view(), {}, 'tournament_detail'),

    url(r'^games/(?P<pk>\d+)/$', GameDetailView.as_view(), {}, 'game_detail'),
    url(r'^games/(?P<pk>\d+)/interested$', interest_in_game, {}, 'game_interest_added'),

    url(r'^profiles/$', PlayerListView.as_view(), {}, 'profile_list'),
    url(r'^profiles/(?P<pk>\d+)/$', PlayerDetailView.as_view(), {}, 'player_detail'),
)

