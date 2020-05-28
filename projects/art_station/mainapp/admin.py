from django.contrib import admin

# Register your models here.

from .models import Artist
from .models import Studio
from .models import ImageInfoArtist

from .models import ImageProfile
from .models import ImageStore

from .models import JobApplication
from .models import JobListing

admin.site.register(Artist)
admin.site.register(Studio)
admin.site.register(ImageInfoArtist)
admin.site.register(ImageProfile)
admin.site.register(ImageStore)
admin.site.register(JobApplication)
admin.site.register(JobListing)