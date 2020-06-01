# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)



class Locality(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    municipal_ward = models.CharField(max_length=20, blank=True, null=True)



class Location(models.Model):
    locality = models.ForeignKey(Locality, models.DO_NOTHING, db_column='locality', blank=True, null=True)
    city = models.ForeignKey('LocationCity', models.DO_NOTHING, db_column='city', blank=True, null=True)
    state = models.ForeignKey('LocationState', models.DO_NOTHING, db_column='state', blank=True, null=True)


class LocationCity(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)



class LocationState(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)



class Property(models.Model):
    seller = models.ForeignKey('Seller', models.DO_NOTHING, db_column='seller', blank=True, null=True)
    type = models.ForeignKey('PropertyType', models.DO_NOTHING, db_column='type', blank=True, null=True)
    address_1 = models.CharField(max_length=300, blank=True, null=True)
    address_2 = models.CharField(max_length=300, blank=True, null=True)
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='location', blank=True, null=True)
    location_lat = models.FloatField(blank=True, null=True)
    location_long = models.FloatField(blank=True, null=True)
    verified = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)



class PropertyHouse(models.Model):
    property = models.ForeignKey(Property, models.DO_NOTHING, db_column='property_ID', blank=True, null=True)  # Field name made lowercase.
    area = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    num_floor = models.IntegerField(blank=True, null=True)
    num_room = models.IntegerField(blank=True, null=True)
    num_kitchen = models.IntegerField(blank=True, null=True)
    num_bathroom = models.IntegerField(blank=True, null=True)
    num_hall = models.IntegerField(blank=True, null=True)
    additional_desc = models.CharField(max_length=1000, blank=True, null=True)



class PropertyLand(models.Model):
    property = models.ForeignKey(Property, models.DO_NOTHING, db_column='property_ID', blank=True, null=True)  # Field name made lowercase.
    area = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    additional_desc = models.CharField(max_length=1000, blank=True, null=True)



class PropertyType(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.



class Seller(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)

