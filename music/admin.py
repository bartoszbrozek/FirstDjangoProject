from django.contrib import admin
from .models import Album, Song
# admin pass1234

admin.site.register(Album)
admin.site.register(Song)