from django.contrib import admin

from users_event.models import Event, Tag, Participant, Rating

# Register your models here.
admin.site.register(Event)
admin.site.register(Tag)
admin.site.register(Participant)
admin.site.register(Rating)
