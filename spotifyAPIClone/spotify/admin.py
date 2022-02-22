from django.contrib import admin
from .models import Track,Artist,Album,Show,Profil,ProfileFollowedArtists
# Register your models here.


admin.site.register(Track)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Show)
admin.site.register(Profil)
admin.site.register(ProfileFollowedArtists)