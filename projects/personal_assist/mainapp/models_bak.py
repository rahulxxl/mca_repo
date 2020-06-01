# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Command(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    command = models.CharField(max_length=255, blank=True, null=True)
    service = models.ForeignKey('Service', models.DO_NOTHING, db_column='service', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'command'


class KeywordMisc(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    keyword = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyword_misc'


class KeywordSecondary(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    keyword = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyword_secondary'


class KeywordsPrimary(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    keyword = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords_primary'


class Service(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    api_key = models.CharField(max_length=511, blank=True, null=True)
    api_url = models.CharField(max_length=1023, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
