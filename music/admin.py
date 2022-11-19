from django.contrib import admin
from .models import *


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'rating', 'album']
    list_filter = ['genres']
    search_fields = ['title', 'singers']


admin.site.register(Singer)
admin.site.register(Genre)
admin.site.register(Album)



