from django.contrib import admin
from .models import PersonUser, TalentUser, VenueUser, Post, Event

# Register your models here.
admin.site.register(PersonUser)
admin.site.register(TalentUser)
admin.site.register(VenueUser)
admin.site.register(Post)
admin.site.register(Event)

