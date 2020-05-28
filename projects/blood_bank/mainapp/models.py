# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BloodGroup(models.Model):
    """ The type of Blood Group"""
    GROUP_TYPE = (
        ("A+", "A+"),
        ("B+", "B+"),
        ("O+", "O+"),
        ("AB+", "AB+"),
        ("A-", "A-"),
        ("B-", "B-"),
        ("O-", "O-"),
        ("AB-", "AB-")        
    )
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    group = models.CharField(max_length=3, blank=True, null=True, choices=GROUP_TYPE)

    def __str__(self):
        return self.group


class BloodIssue(models.Model):
    """ Record for which Blood unit has been given to whom """
    BUYER_TYPE = (
        ("Person", "Person"),
        ("Hospital", "Hospital")
    )

    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    group = models.ForeignKey(BloodGroup, models.DO_NOTHING, blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    buyer = models.CharField(max_length=12, blank=True, null=True, choices=BUYER_TYPE)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Donor(models.Model):
    """ The Donor who has donated blood to the bank"""
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    blood_group = models.ForeignKey(BloodGroup, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name


class BloodUnit(models.Model):
    """ Detail of each blood unit that is present in the blood bank"""
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(BloodGroup, models.DO_NOTHING, blank=True, null=True)
    donor = models.ForeignKey(Donor, models.DO_NOTHING, blank=True, null=True)

    test_abo = models.BooleanField(blank=True, null=True)
    test_rh = models.BooleanField(blank=True, null=True)
    test_antibody = models.BooleanField(blank=True, null=True)
    test_hep_b = models.BooleanField(blank=True, null=True)
    test_hep_c = models.BooleanField(blank=True, null=True)
    test_alt = models.BooleanField(blank=True, null=True)
    test_htlv = models.BooleanField(blank=True, null=True)
    test_hiv = models.BooleanField(blank=True, null=True)
    test_passed = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.group


class Camp(models.Model):
    """ Details of the Camp Organized """
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    location = models.CharField(max_length=300, blank=True, null=True)
    location_lat = models.FloatField(blank=True, null=True)
    location_long = models.FloatField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    unit_a_pos = models.IntegerField(blank=True, null=True)
    unit_b_pos = models.IntegerField(blank=True, null=True)
    unit_o_pos = models.IntegerField(blank=True, null=True)
    unit_ab_pos = models.IntegerField(blank=True, null=True)
    unit_a_neg = models.IntegerField(blank=True, null=True)
    unit_b_neg = models.IntegerField(blank=True, null=True)
    unit_o_neg = models.IntegerField(blank=True, null=True)
    unit_ab_neg = models.IntegerField(blank=True, null=True)
    total_donors = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.location


class Inventory(models.Model):
    """ Current Inventory of the Blood Bank """
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(BloodGroup, models.DO_NOTHING, blank=True, null=True)
    units = models.IntegerField(blank=True, null=True)
    min_units = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.group
