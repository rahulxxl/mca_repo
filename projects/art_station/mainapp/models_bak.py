# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    subscription = models.ForeignKey('Subscription', models.DO_NOTHING, db_column='subscription', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist'


class City(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    state = models.ForeignKey('State', models.DO_NOTHING, db_column='state', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class ImageInfoArtist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    owner = models.ForeignKey(Artist, models.DO_NOTHING, db_column='owner', blank=True, null=True)
    image_store = models.ForeignKey('ImageStore', models.DO_NOTHING, db_column='image_store', blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    medium = models.CharField(max_length=255, blank=True, null=True)
    software = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_info_artist'


class ImageInfoStudio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    owner = models.ForeignKey('Studio', models.DO_NOTHING, db_column='owner', blank=True, null=True)
    image_store = models.ForeignKey('ImageStore', models.DO_NOTHING, db_column='image_store', blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    medium = models.CharField(max_length=255, blank=True, null=True)
    software = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_info_studio'


class ImageProfile(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_profile'


class ImageStore(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    image = models.TextField(blank=True, null=True)
    thumb_image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_store'


class JobApplication(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    job_listing = models.ForeignKey('JobListing', models.DO_NOTHING, db_column='job_listing', blank=True, null=True)
    artist = models.ForeignKey(Artist, models.DO_NOTHING, db_column='artist', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_application'


class JobListing(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100, blank=True, null=True)
    short_desc = models.CharField(max_length=255, blank=True, null=True)
    long_desc = models.CharField(max_length=2000, blank=True, null=True)
    expirience = models.CharField(max_length=50, blank=True, null=True)
    studio = models.ForeignKey('Studio', models.DO_NOTHING, db_column='studio', blank=True, null=True)
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='location', blank=True, null=True)
    salary = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    applicants = models.IntegerField(blank=True, null=True)
    additional_info = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_listing'


class Location(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    studio = models.ForeignKey('Studio', models.DO_NOTHING, db_column='studio', blank=True, null=True)
    address_1 = models.CharField(max_length=255, blank=True, null=True)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city', blank=True, null=True)
    state = models.ForeignKey('State', models.DO_NOTHING, db_column='state', blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='country', blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    location_lat = models.DecimalField(max_digits=19, decimal_places=16, blank=True, null=True)
    location_long = models.DecimalField(max_digits=19, decimal_places=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class State(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='country', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'


class Studio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    subscription = models.ForeignKey('Subscription', models.DO_NOTHING, db_column='subscription', blank=True, null=True)
    profile_image = models.ForeignKey(ImageProfile, models.DO_NOTHING, db_column='profile_image', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studio'


class Subscription(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription'
