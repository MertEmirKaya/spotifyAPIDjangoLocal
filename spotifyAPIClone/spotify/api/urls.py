from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TrackAPIViewSet,ArtistAPIViewSet,AlbumAPIViewSet
route=DefaultRouter()
route.register(r'tracks',TrackAPIViewSet)
route.register(r'artists',ArtistAPIViewSet)
route.register(r'albums',AlbumAPIViewSet)


urlpatterns = [
    path('',include(route.urls)),
]