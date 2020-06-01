# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

ART_SOFTWARE =(
    ("photshop","Photoshop"),
    ("zbrush","ZBrush"),
    ("blender","Blender"),
    ("maya","Maya"),
    ("3ds_max","3DS max"),
)

ART_MEDIUM = (
    ("2d_Drawing","2D Drawing"),
    ("3d_Model","3D model"),
    ("hand_painting","Hand Painting"),
)


class Artist(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name

    
class ImageProfile(models.Model):
    image = models.ImageField(blank=True, null=True)
    owner = models.ForeignKey(Artist, models.DO_NOTHING, blank=True, null=True)



class ImageInfoArtist(models.Model):
    desc = models.CharField(max_length=255, blank=True, null=True)


class ImageStore(models.Model):
    image = models.ImageField(blank=True, null=True)
    owner = models.ForeignKey(Artist, models.DO_NOTHING, blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    medium = models.CharField(max_length=255, blank=True, null=True)
    software = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        if self.owner is not None:
            return self.owner.name
        return "Missing Artist Name"


class JobApplication(models.Model):
    job_listing = models.ForeignKey('JobListing', models.DO_NOTHING, db_column='job_listing', blank=True, null=True)
    artist = models.ForeignKey(Artist, models.DO_NOTHING, db_column='artist', blank=True, null=True)

   
class JobListing(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=50, blank=True, null=True)
    studio = models.ForeignKey('Studio', models.DO_NOTHING, db_column='studio', blank=True, null=True)
    salary = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return self.desc
    

class Studio(models.Model):
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ForeignKey(ImageProfile, models.DO_NOTHING, db_column='profile_image', blank=True, null=True)

    def __str__(self):
        return self.name


class ArtistLogin(models.Model):
    username = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank =False, null=False)
    artist = models.ForeignKey(Artist, models.DO_NOTHING, blank=False, null=False)

    def __str__(self):
        return username