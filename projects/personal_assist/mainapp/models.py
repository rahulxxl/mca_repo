# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Command(models.Model):
    command = models.CharField(max_length=255, blank=True, null=True)
    service = models.ForeignKey('Service', models.DO_NOTHING, db_column='service', blank=True, null=True)



class KeywordMisc(models.Model):
    keyword = models.CharField(max_length=30, blank=True, null=True)



class KeywordSecondary(models.Model):
    keyword = models.CharField(max_length=30, blank=True, null=True)



class KeywordsPrimary(models.Model):
    keyword = models.CharField(max_length=30, blank=True, null=True)



class Service(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    api_key = models.CharField(max_length=511, blank=True, null=True)
    api_url = models.CharField(max_length=1023, blank=True, null=True)



class User(models.Model):
    user_name = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

