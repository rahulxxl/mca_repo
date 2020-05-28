from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(DevSkill)
admin.site.register(Developer)
admin.site.register(ImageStore)
admin.site.register(Jam)
admin.site.register(JamOrganizer)
admin.site.register(JamTeam)
admin.site.register(Skill)
admin.site.register(Studio)
admin.site.register(Team)