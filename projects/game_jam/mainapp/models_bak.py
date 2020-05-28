# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DevSkill(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    developer = models.ForeignKey('Developer', models.DO_NOTHING, db_column='developer', blank=True, null=True)
    skill = models.ForeignKey('Skill', models.DO_NOTHING, db_column='skill', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dev_skill'


class Developer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ForeignKey('ImageStore', models.DO_NOTHING, db_column='profile_image', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'developer'


class ImageStore(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_store'


class Jam(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    theme = models.CharField(max_length=50, blank=True, null=True)
    team_size = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    prize = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jam'


class JamOrganizer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    jam = models.ForeignKey(Jam, models.DO_NOTHING, db_column='jam', blank=True, null=True)
    studio = models.ForeignKey('Studio', models.DO_NOTHING, db_column='studio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jam_organizer'


class JamTeam(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    team = models.ForeignKey('Team', models.DO_NOTHING, db_column='team', blank=True, null=True)
    jam = models.ForeignKey(Jam, models.DO_NOTHING, db_column='jam', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jam_team'


class Skill(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    skill = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill'


class Studio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ForeignKey(ImageStore, models.DO_NOTHING, db_column='profile_image', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studio'


class Team(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    dev_leader = models.ForeignKey(Developer, models.DO_NOTHING, db_column='dev_leader', blank=True, null=True)
    dev_2 = models.ForeignKey(Developer, models.DO_NOTHING, db_column='dev_2', blank=True, null=True)
    dev_3 = models.ForeignKey(Developer, models.DO_NOTHING, db_column='dev_3', blank=True, null=True)
    dev_4 = models.ForeignKey(Developer, models.DO_NOTHING, db_column='dev_4', blank=True, null=True)
    dev_5 = models.ForeignKey(Developer, models.DO_NOTHING, db_column='dev_5', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'
