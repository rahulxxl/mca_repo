# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Booking(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey('Customer', models.DO_NOTHING, db_column='customer', blank=True, null=True)
    room = models.ForeignKey('HotelRoom', models.DO_NOTHING, db_column='room', blank=True, null=True)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_of_adult = models.IntegerField(blank=True, null=True)
    num_of_children = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking'


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


class Customer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Hotel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    locality = models.ForeignKey('Locality', models.DO_NOTHING, db_column='locality', blank=True, null=True)
    gps_lat = models.FloatField(blank=True, null=True)
    gps_long = models.FloatField(blank=True, null=True)
    image = models.ForeignKey('ImageHotel', models.DO_NOTHING, db_column='image', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel'


class HotelRoom(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hotel', blank=True, null=True)
    room_type = models.ForeignKey('RoomType', models.DO_NOTHING, db_column='room_type', blank=True, null=True)
    facility = models.ForeignKey('RoomFacility', models.DO_NOTHING, db_column='facility', blank=True, null=True)
    num_of_adults = models.IntegerField(blank=True, null=True)
    num_of_children = models.IntegerField(blank=True, null=True)
    image = models.ForeignKey('ImageRoom', models.DO_NOTHING, db_column='image', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel_room'


class ImageHotel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    image_1 = models.TextField(blank=True, null=True)
    image_2 = models.TextField(blank=True, null=True)
    image_3 = models.TextField(blank=True, null=True)
    image_4 = models.TextField(blank=True, null=True)
    image_5 = models.TextField(blank=True, null=True)
    image_6 = models.TextField(blank=True, null=True)
    image_7 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_hotel'


class ImageRoom(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    image_1 = models.TextField(blank=True, null=True)
    image_2 = models.TextField(blank=True, null=True)
    image_3 = models.TextField(blank=True, null=True)
    image_4 = models.TextField(blank=True, null=True)
    image_5 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_room'


class Locality(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=150, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city', blank=True, null=True)
    gps_lat = models.FloatField(blank=True, null=True)
    gps_long = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locality'


class Rating(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hotel', blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer', blank=True, null=True)
    overall_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'


class Review(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hotel', blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer', blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    desc = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class RoomFacility(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ac = models.IntegerField(blank=True, null=True)
    wifi = models.IntegerField(blank=True, null=True)
    swimming_pool = models.IntegerField(blank=True, null=True)
    bar = models.IntegerField(blank=True, null=True)
    resturaunt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_facility'


class RoomType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(max_length=100, blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    facility = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_type'


class State(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='country', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'
