from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TrackAPIViewSet,ArtistAPIViewSet,AlbumAPIViewSet,ShowAPIViewSet,ProfilAPIViewSet,ProfilTopTracksListAPIView,ProfilTopArtistsListAPIView,ProfileFollowedArtistsListAPIView
route=DefaultRouter()
route.register(r'tracks',TrackAPIViewSet)
route.register(r'artists',ArtistAPIViewSet)
route.register(r'albums',AlbumAPIViewSet)
route.register(r'shows',ShowAPIViewSet)
route.register(r'profiles',ProfilAPIViewSet)

urlpatterns = [
    path('',include(route.urls)),
    path('me/tracks',ProfilTopTracksListAPIView.as_view()),
    path('me/artists',ProfilTopArtistsListAPIView.as_view()),
    path('me/following',ProfileFollowedArtistsListAPIView.as_view()),
    
]