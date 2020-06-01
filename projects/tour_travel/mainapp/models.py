# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Booking(models.Model):
    customer = models.ForeignKey(
        'Customer', models.DO_NOTHING, db_column='customer', blank=True, null=True)
    room = models.ForeignKey(
        'HotelRoom', models.DO_NOTHING, db_column='room', blank=True, null=True)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    num_of_adult = models.IntegerField(blank=True, null=True)
    num_of_children = models.IntegerField(blank=True, null=True)


class Customer(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    locality = models.ForeignKey('Locality', models.DO_NOTHING, db_column='locality', blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    # gps_lat = models.FloatField(blank=True, null=True)
    # gps_long = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class HotelRoom(models.Model):
    ROOM_TYPES=(
        ("delux","Delux"),
        ("premium","Premium"),
        ("delux_lounge","Delux Lounge"),
    )
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING,db_column='hotel', blank=True, null=True)
    room_type = models.CharField(max_length=50, blank=True, null=True, choices=ROOM_TYPES)
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # facility = models.ForeignKey('RoomFacility', models.DO_NOTHING, db_column='facility', blank=True, null=True)
    # num_of_adults = models.IntegerField(blank=True, null=True)
    # num_of_children = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.room_type


class ImageHotel(models.Model):
    image_1 = models.TextField(blank=True, null=True)
    image_2 = models.TextField(blank=True, null=True)
    image_3 = models.TextField(blank=True, null=True)
    image_4 = models.TextField(blank=True, null=True)
    image_5 = models.TextField(blank=True, null=True)
    image_6 = models.TextField(blank=True, null=True)
    image_7 = models.TextField(blank=True, null=True)


class ImageRoom(models.Model):
    image_1 = models.TextField(blank=True, null=True)
    image_2 = models.TextField(blank=True, null=True)
    image_3 = models.TextField(blank=True, null=True)
    image_4 = models.TextField(blank=True, null=True)
    image_5 = models.TextField(blank=True, null=True)


class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)


class City(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    state = models.ForeignKey(
        'State', models.DO_NOTHING, db_column='state', blank=True, null=True)


class Locality(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING,
                             db_column='city', blank=True, null=True)
    gps_lat = models.FloatField(blank=True, null=True)
    gps_long = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING,
                              db_column='hotel', blank=True, null=True)
    customer = models.ForeignKey(
        Customer, models.DO_NOTHING, db_column='customer', blank=True, null=True)
    overall_rating = models.DecimalField(
        max_digits=2, decimal_places=1, blank=True, null=True)


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING,
                              db_column='hotel', blank=True, null=True)
    customer = models.ForeignKey(
        Customer, models.DO_NOTHING, db_column='customer', blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    desc = models.CharField(max_length=2000, blank=True, null=True)


class RoomFacility(models.Model):
    ac = models.IntegerField(blank=True, null=True)
    wifi = models.IntegerField(blank=True, null=True)
    swimming_pool = models.IntegerField(blank=True, null=True)
    bar = models.IntegerField(blank=True, null=True)
    resturaunt = models.IntegerField(blank=True, null=True)


class RoomType(models.Model):
    type = models.CharField(max_length=100, blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    facility = models.IntegerField(blank=True, null=True)


class State(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(
        Country, models.DO_NOTHING, db_column='country', blank=True, null=True)
