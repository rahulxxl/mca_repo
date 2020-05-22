# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BloodGroup(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    group = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        db_table = 'blood_group'


class BloodIssue(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    group = models.IntegerField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'blood_issue'


class IdProof(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    proof_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'id_proof'


class Donor(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    id_proof = models.ForeignKey(IdProof, models.DO_NOTHING, db_column='id_proof', blank=True, null=True)
    id_number = models.CharField(max_length=30, blank=True, null=True)
    blood_group = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'donor'


class BloodUnit(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    group = models.ForeignKey(BloodGroup, models.DO_NOTHING, db_column='group', blank=True, null=True)
    donor = models.ForeignKey(Donor, models.DO_NOTHING, db_column='donor', blank=True, null=True)
    test_abo = models.IntegerField(blank=True, null=True)
    test_rh = models.IntegerField(blank=True, null=True)
    test_antibody = models.IntegerField(blank=True, null=True)
    test_hep_b = models.IntegerField(blank=True, null=True)
    test_hep_c = models.IntegerField(blank=True, null=True)
    test_alt = models.IntegerField(blank=True, null=True)
    test_htlv = models.IntegerField(blank=True, null=True)
    test_hiv = models.IntegerField(blank=True, null=True)
    test_passed = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'blood_unit'


class Camp(models.Model):
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

    class Meta:
        db_table = 'camp'



class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(BloodGroup, models.DO_NOTHING, blank=True, null=True)
    units = models.IntegerField(blank=True, null=True)
    min_units = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'inventory'
