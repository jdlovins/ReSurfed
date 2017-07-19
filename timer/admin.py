from django.contrib import admin
from .models import Map, Player, Server, Time, CheckpointTime, Recording, MapStatistic, PlayerOption, Spawn, PlayerStatistic, Zone, MapConfiguration

admin.site.register(Map)
admin.site.register(Player)
admin.site.register(Server)
admin.site.register(Time)
admin.site.register(CheckpointTime)
admin.site.register(Recording)
admin.site.register(MapStatistic)
admin.site.register(PlayerOption)
admin.site.register(Spawn)
admin.site.register(PlayerStatistic)
admin.site.register(Zone)
admin.site.register(MapConfiguration)