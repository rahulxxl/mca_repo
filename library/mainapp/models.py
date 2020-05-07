# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    author_1 = models.CharField(max_length=50, blank=True, null=True)
    author_2 = models.CharField(max_length=50, blank=True, null=True)
    author_3 = models.CharField(max_length=50, blank=True, null=True)
    author_4 = models.CharField(max_length=50, blank=True, null=True)
    author_5 = models.CharField(max_length=50, blank=True, null=True)
    author_6 = models.CharField(max_length=50, blank=True, null=True)
    author_7 = models.CharField(max_length=50, blank=True, null=True)
    author_8 = models.CharField(max_length=50, blank=True, null=True)
    author_9 = models.CharField(max_length=50, blank=True, null=True)
    author_10 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author'


class Book(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    book_master = models.ForeignKey('BookMaster', models.DO_NOTHING, db_column='book_master', blank=True, null=True)
    shelf = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class BookMaster(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    author = models.IntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'book_master'


class Student(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
