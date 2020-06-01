# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Award(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    match = models.ForeignKey('Match', models.DO_NOTHING, db_column='match', blank=True, null=True)
    first_prize = models.IntegerField(blank=True, null=True)
    second_prize = models.IntegerField(blank=True, null=True)
    third_price = models.IntegerField(blank=True, null=True)
    per_kill = models.IntegerField(blank=True, null=True)
    first_team = models.ForeignKey('PubgTeam', models.DO_NOTHING, db_column='first_team', blank=True, null=True)
    second_team = models.ForeignKey('PubgTeam', models.DO_NOTHING, db_column='second_team', blank=True, null=True)
    third_team = models.ForeignKey('PubgTeam', models.DO_NOTHING, db_column='third_team', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'award'


class Gamer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=60, blank=True, null=True)
    pubg_id = models.CharField(db_column='pubg_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    pubg_name = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING, db_column='payment_method', blank=True, null=True)
    acc_num = models.CharField(max_length=50, blank=True, null=True)
    ifscode = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamer'


class Match(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    team_type = models.ForeignKey('TeamType', models.DO_NOTHING, db_column='team_type', blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    room_id = models.CharField(db_column='room_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=20, blank=True, null=True)
    entry_charge = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'match'


class PaymentMethod(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    desc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_method'


class PubgTeam(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30, blank=True, null=True)
    team_type = models.ForeignKey('TeamType', models.DO_NOTHING, db_column='team_type', blank=True, null=True)
    player_1 = models.ForeignKey(Gamer, models.DO_NOTHING, db_column='player_1', blank=True, null=True)
    player_2 = models.ForeignKey(Gamer, models.DO_NOTHING, db_column='player_2', blank=True, null=True)
    player_3 = models.ForeignKey(Gamer, models.DO_NOTHING, db_column='player_3', blank=True, null=True)
    player_4 = models.ForeignKey(Gamer, models.DO_NOTHING, db_column='player_4', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pubg_team'


class TeamType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(max_length=5, blank=True, null=True)
    max_player = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_type'
