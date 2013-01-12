from tournament.resources import PlayerResource, TournamentResource, GameResource, ComputerResource, PlatformResource, TeamResource
from rest_api.apis import raw

raw.api.register(PlayerResource())
raw.api.register(TournamentResource())
raw.api.register(GameResource())
raw.api.register(ComputerResource())
raw.api.register(PlatformResource())
raw.api.register(TeamResource())
