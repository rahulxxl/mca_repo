# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CategoryMain(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    category_root = models.ForeignKey('CategoryRoot', models.DO_NOTHING, db_column='category_root', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_main'


class CategoryRoot(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_root'


class CategorySub(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    category_main = models.ForeignKey(CategoryMain, models.DO_NOTHING, db_column='category_main', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_sub'


class CategoryVariant(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    category_sub = models.ForeignKey(CategorySub, models.DO_NOTHING, db_column='category_sub', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_variant'


class Customer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=70, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    gstin = models.CharField(db_column='GSTIN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    primary_location = models.ForeignKey('Location', models.DO_NOTHING, db_column='primary_location', blank=True, null=True)
    seller_service = models.ForeignKey('SellerService', models.DO_NOTHING, db_column='seller_service', blank=True, null=True)
    subscription = models.ForeignKey('Subscription', models.DO_NOTHING, db_column='subscription', blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=21, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class DeliveryStatus(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery_status'


class ImageStore(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_store'


class Item(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='product', blank=True, null=True)
    category_root = models.ForeignKey(CategoryRoot, models.DO_NOTHING, db_column='category_root', blank=True, null=True)
    category_main = models.ForeignKey(CategoryMain, models.DO_NOTHING, db_column='category_main', blank=True, null=True)
    category_sub = models.ForeignKey(CategorySub, models.DO_NOTHING, db_column='category_sub', blank=True, null=True)
    category_variant = models.ForeignKey(CategoryVariant, models.DO_NOTHING, db_column='category_variant', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    mapper_ebay = models.IntegerField(blank=True, null=True)
    mapper_snapdeal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


class Location(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.ForeignKey('LocationCity', models.DO_NOTHING, db_column='city', blank=True, null=True)
    pin_code = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class LocationCity(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    location_state = models.ForeignKey('LocationState', models.DO_NOTHING, db_column='location_state', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_city'


class LocationState(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_state'


class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    item = models.ForeignKey(Item, models.DO_NOTHING, db_column='item', blank=True, null=True)
    shipping_1 = models.CharField(max_length=200, blank=True, null=True)
    shipping_2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.ForeignKey(LocationCity, models.DO_NOTHING, db_column='city', blank=True, null=True)
    delivery = models.ForeignKey(DeliveryStatus, models.DO_NOTHING, db_column='delivery', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    long_description = models.CharField(max_length=1000, blank=True, null=True)
    mapper_ebay = models.IntegerField(blank=True, null=True)
    mapper_snapdeal = models.IntegerField(blank=True, null=True)
    image_1 = models.ForeignKey(ImageStore, models.DO_NOTHING, db_column='image_1', blank=True, null=True)
    image_2 = models.ForeignKey(ImageStore, models.DO_NOTHING, db_column='image_2', blank=True, null=True)
    image_3 = models.ForeignKey(ImageStore, models.DO_NOTHING, db_column='image_3', blank=True, null=True)
    image_4 = models.ForeignKey(ImageStore, models.DO_NOTHING, db_column='image_4', blank=True, null=True)
    image_5 = models.ForeignKey(ImageStore, models.DO_NOTHING, db_column='image_5', blank=True, null=True)
    image_6 = models.ForeignKey(ImageStore, models.DO_NOTHING, db_column='image_6', blank=True, null=True)
    image_7 = models.ForeignKey(ImageStore, models.DO_NOTHING, db_column='image_7', blank=True, null=True)
    image_8 = models.ForeignKey(ImageStore, models.DO_NOTHING, db_column='image_8', blank=True, null=True)
    image_9 = models.ForeignKey(ImageStore, models.DO_NOTHING, db_column='image_9', blank=True, null=True)
    image_10 = models.ForeignKey(ImageStore, models.DO_NOTHING, db_column='image_10', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class SellerService(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seller_service'


class Subscription(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription'
