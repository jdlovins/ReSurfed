from django.db import models


class Map(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    difficulty = models.IntegerField()
    checkpoints = models.SmallIntegerField()
    type = models.IntegerField()
    author = models.CharField(max_length=50, blank=True)
    bonuses = models.SmallIntegerField()
    active = models.IntegerField()
    prevent_prehop = models.IntegerField()
    enable_baked_triggers = models.IntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    steam_id = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50, blank=True)
    ip = models.CharField(max_length=50, blank=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

    def __str__(self):
        return "%s (%s)" % (self.name, self.steam_id)


class Server(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(unique=True, max_length=32)
    name = models.CharField(max_length=64, blank=True)
    date_created = models.DateTimeField()
    current_map = models.CharField(max_length=64, blank=True)
    bots_enabled = models.IntegerField()
    key = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name


class Time(models.Model):
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey(Map, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    type = models.SmallIntegerField()
    stage = models.SmallIntegerField()
    time = models.FloatField()
    rank = models.IntegerField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    server = models.ForeignKey(Server)
    completions = models.IntegerField()
    best_rank = models.IntegerField()
    date_demoted = models.DateTimeField()

    class Meta:
        unique_together = (('map', 'player', 'stage', 'type'),)
        index_together = (('map', 'type', 'stage'),)

    def __str__(self):
        return "%s - %s (Type: %s, Stage: %s)" % (self.player, self.map, self.type, self.stage)


class CheckpointTime(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    map = models.ForeignKey(Map, on_delete=models.PROTECT)
    zone = models.SmallIntegerField()
    time = models.FloatField()
    stage_time = models.FloatField()
    velocity = models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = (('player', 'map', 'zone'),)


class Recording(models.Model):
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey(Map, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    stage = models.IntegerField()
    type = models.IntegerField()
    time = models.FloatField()
    date_created = models.DateTimeField()
    is_uploaded = models.IntegerField()
    is_deleted = models.IntegerField()
    length = models.IntegerField()


class MapStatistic(models.Model):
    map = models.OneToOneField(Map, primary_key=True, on_delete=models.CASCADE)
    completions = models.IntegerField()
    stage_points = models.IntegerField()
    bonus_points = models.IntegerField()
    map_points = models.IntegerField()
    stage_record_points = models.IntegerField()
    bonus_record_points = models.IntegerField()


class PlayerOption(models.Model):
    player = models.OneToOneField(Player, primary_key=True, on_delete=models.CASCADE)
    hud_config = models.CharField(max_length=32, blank=True)
    hide_panel = models.IntegerField()
    sounds = models.IntegerField()
    color_scheme = models.IntegerField()
    chat_mode = models.IntegerField()
    teleport_velocity = models.IntegerField()


class Spawn(models.Model):
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    zone = models.SmallIntegerField()
    type = models.SmallIntegerField()
    origin = models.CharField(max_length=75)
    angle = models.CharField(max_length=75)
    velocity = models.CharField(max_length=75)

    class Meta:
        unique_together = (('map', 'zone', 'type'),)


class PlayerStatistic(models.Model):
    player = models.OneToOneField(Player, primary_key=True, on_delete=models.CASCADE)
    percent_complete = models.FloatField()
    complete_maps = models.IntegerField()
    complete_stages = models.IntegerField()
    complete_bonuses = models.IntegerField()
    map_records = models.IntegerField()
    stage_records = models.IntegerField()
    bonus_records = models.IntegerField()
    map_tops = models.IntegerField()
    completion_points = models.IntegerField()
    top_points = models.IntegerField()
    group_points = models.DecimalField(max_digits=15, decimal_places=2)
    map_completion_points = models.IntegerField()
    stage_completion_points = models.IntegerField()
    bonus_completion_points = models.IntegerField()
    top_record_points = models.IntegerField()
    stage_record_points = models.IntegerField()
    bonus_record_points = models.IntegerField()


class Zone(models.Model):
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    min_cord = models.CharField(max_length=75)
    max_cord = models.CharField(max_length=75)
    target_name = models.CharField(max_length=32, blank=True)
    filter_name = models.CharField(max_length=32, blank=True)
    type = models.IntegerField()
    value = models.IntegerField()
    velocity = models.IntegerField()


class MapConfiguration(models.Model):
    map = models.OneToOneField(Map, primary_key=True, on_delete=models.CASCADE)
    config = models.CharField(max_length=20000, blank=True, null=True)
