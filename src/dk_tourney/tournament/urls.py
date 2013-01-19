from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from tournament.views import GameListView, GameDetailView, interest_in_game, PlayerListView, PlayerDetailView, PlayerEditView, PlayerCreateView, TeamListView, TeamDetailView, TeamEditView, TeamCreateView, TeamInviteCreateView, ComputerEditView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^games/$', GameListView.as_view(), {}, 'game_list'),
    url(r'^games/(?P<pk>\d+)/$', GameDetailView.as_view(), {}, 'game_detail'),
    url(r'^games/(?P<pk>\d+)/interested$', interest_in_game, {}, 'game_interest_added'),

    url(r'^players/$', PlayerListView.as_view(), {}, 'player_list'),
    url(r'^players/(?P<pk>\d+)/$', PlayerDetailView.as_view(), {}, 'player_detail'),
    url(r'^players/(?P<pk>\d+)/edit$', login_required(PlayerEditView.as_view()), {}, 'player_edit'),
    url(r'^players/(?P<pk>\d+)/create$', login_required(PlayerCreateView.as_view()), {}, 'player_create'),

    url(r'^teams/$', TeamListView.as_view(), {}, 'team_list'),
    url(r'^teams/(?P<pk>\d+)/$', TeamDetailView.as_view(), {}, 'team_detail'),
    url(r'^teams/(?P<pk>\d+)/edit$', login_required(TeamEditView.as_view()), {}, 'team_edit'),
    url(r'^teams/(?P<pk>\d+)/create$', login_required(TeamCreateView.as_view()), {}, 'team_create'),
    url(r'^teams/(?P<pk>\d+)/invite$', login_required(TeamInviteCreateView.as_view()), {}, 'teaminvite_create'),
    url(r'^teams/(?P<pk>\d+)/invite$', login_required(TeamInviteCreateView.as_view()), {}, 'teaminvite_accept'),

    url(r'^computers/(?P<pk>\d+)/edit$', login_required(ComputerEditView.as_view()), {}, 'computer_edit'),
)

