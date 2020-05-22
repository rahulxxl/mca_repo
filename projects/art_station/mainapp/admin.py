from django.contrib import admin

# Register your models here.

from .models import Artist
from .models import Studio
from .models import ImageInfoArtist
from .models import ImageInfoStudio
from .models import ImageProfile
from .models import ImageStore
from .models import Subscription
from .models import JobApplication
from .models import JobListing
from .models import Location
from .models import City
from .models import Country
from .models import State
from .models import ImageMainStore


admin.site.register(Artist)
admin.site.register(Studio)
admin.site.register(ImageInfoArtist)
admin.site.register(ImageInfoStudio)
admin.site.register(ImageProfile)
admin.site.register(ImageStore)
admin.site.register(Subscription)
admin.site.register(JobApplication)
admin.site.register(JobListing)
admin.site.register(Location)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(ImageMainStore)