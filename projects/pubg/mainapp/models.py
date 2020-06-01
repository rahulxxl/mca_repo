# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

PAYMENT_METHODS=(
    ("google_pay","Google Pay"),
    ("paytm","Paytm"),
)

TEAM_TYPE=(
    ("solo","Solo"),
    ("duo","Duo"),
    ("squad","Squad"),
)


# class Award(models.Model):
#     match = models.ForeignKey('Match', models.DO_NOTHING, db_column='match', blank=True, null=True)
#     first_prize = models.IntegerField(blank=True, null=True)
#     second_prize = models.IntegerField(blank=True, null=True)
#     third_price = models.IntegerField(blank=True, null=True)
#     per_kill = models.IntegerField(blank=True, null=True)
#     first_team = models.ForeignKey('PubgTeam', models.DO_NOTHING, related_name='award_first_team', blank=True, null=True)
#     second_team = models.ForeignKey('PubgTeam', models.DO_NOTHING,related_name='award_second_team', blank=True, null=True)
#     third_team = models.ForeignKey('PubgTeam', models.DO_NOTHING, related_name='award_third_team', blank=True, null=True)


class Gamer(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    pubg_id = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    pubg_name = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    payment_method = models.CharField(max_length = 20, blank=True, null=True, choices=PAYMENT_METHODS)
    acc_num = models.CharField(max_length=50, blank=True, null=True)
    ifscode = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Match(models.Model):
    start_date = models.DateTimeField(blank=True, null=True)
    team_type = models.CharField(max_length=10, blank=True, null=True, choices= TEAM_TYPE)
    room_id = models.CharField(max_length=20, blank=True, null=True)  # Field name made lowercase.
    entry_charge = models.IntegerField(blank=True, null=True)
    win_prize = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.id


class PubgTeam(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    team_type = models.CharField(max_length=10, blank=True, null=True, choices=TEAM_TYPE)
    player_1 = models.ForeignKey(Gamer, models.DO_NOTHING, related_name='team_player_1', blank=True, null=True)
    player_2 = models.ForeignKey(Gamer, models.DO_NOTHING, related_name='team_player_2', blank=True, null=True)
    player_3 = models.ForeignKey(Gamer, models.DO_NOTHING, related_name='team_player_3', blank=True, null=True)
    player_4 = models.ForeignKey(Gamer, models.DO_NOTHING, related_name='team_player_4', blank=True, null=True)

    def __str__(self):
        return self.name
