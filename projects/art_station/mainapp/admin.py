from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Artist)
admin.site.register(Studio)
admin.site.register(ImageStore)
admin.site.register(JobApplication)
admin.site.register(JobListing)
admin.site.register(ActiveSession)
