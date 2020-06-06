# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DevSkill(models.Model):
    developer = models.ForeignKey('Developer', models.DO_NOTHING, blank=True, null=True)
    skill = models.ForeignKey('Skill', models.DO_NOTHING, blank=True, null=True)


class Developer(models.Model):
    username = models.CharField(unique=True, max_length=50, blank=False, null=False)
    name = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username


class ImageStore(models.Model):
    image = models.ImageField(blank=True, null=True)
    developer =  models.ForeignKey(Developer, models.DO_NOTHING, blank=True, null=True)
    
    def __str__(self):
        if self.developer is not None:
            return self.id + "-"+ self.developer.username 
        return "Missing Developer"


class Jam(models.Model):
    theme = models.CharField(max_length=50, blank=True, null=True)
    team_size = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    prize = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    studio = models.ForeignKey('Studio', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.theme


class JamOrganizer(models.Model):
    jam = models.ForeignKey(Jam, models.DO_NOTHING, blank=True, null=True)
    studio = models.ForeignKey('Studio', models.DO_NOTHING, blank=True, null=True)


class JamTeam(models.Model):
    team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True)
    jam = models.ForeignKey(Jam, models.DO_NOTHING, blank=True, null=True)


class Skill(models.Model):
    skill = models.CharField(max_length=50, blank=True, null=True)


class Studio(models.Model):
    username = models.CharField(max_length=50, blank=False, null=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    dev_leader = models.ForeignKey(Developer, models.DO_NOTHING, related_name="dev_leader_to_dev", blank=True, null=True)
    dev_2 = models.ForeignKey(Developer, models.DO_NOTHING, related_name="dev_2_to_dev", blank=True, null=True)
    dev_3 = models.ForeignKey(Developer, models.DO_NOTHING, related_name="dev_3_to_dev", blank=True, null=True)
    dev_4 = models.ForeignKey(Developer, models.DO_NOTHING, related_name="dev_4_to_dev", blank=True, null=True)
    dev_5 = models.ForeignKey(Developer, models.DO_NOTHING, related_name="dev_5_to_dev", blank=True, null=True)


class SessionDeveloper(models.Model):
    developer = models.ForeignKey(Developer, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.developer.username


class SessionStudio(models.Model):
    studio = models.ForeignKey(Studio, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.studio.username


