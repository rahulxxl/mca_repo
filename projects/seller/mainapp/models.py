# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


CATEGORY=(
    ("mobile","Mobile"),
    ("laptops","Laptop"),
    ("clothing","Clothing"),
    ("food","Food"),
)


class Customer(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    gstin = models.CharField(max_length=15, blank=True, null=True)  # Field name made lowercase.
    primary_location = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phome = models.CharField(max_length=15, blank=True, null=True)

class Product(models.Model):
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.CharField(max_length=140, blank=True, null=True)
    full_description = models.CharField(max_length=1000, blank=True, null=True)
    category= models.CharField(max_length=50, blank=True, null=True, choices=CATEGORY)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    image_1 = models.ImageField( blank=True, null=True)
    image_2 = models.ImageField( blank=True, null=True)
    image_3 = models.ImageField( blank=True, null=True)
    image_4 = models.ImageField( blank=True, null=True)

