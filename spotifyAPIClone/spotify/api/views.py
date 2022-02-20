from .serializers import TrackSerializer,ArtistSerializer,AlbumSerializer
from spotify.models import Track,Artist,Album
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

class TrackAPIViewSet(ModelViewSet):
    queryset=Track.objects.all()
    serializer_class=TrackSerializer


class ArtistAPIViewSet(ModelViewSet):
    queryset=Artist.objects.all()
    serializer_class=ArtistSerializer



class AlbumAPIViewSet(ModelViewSet):
    queryset=Album.objects.all()
    serializer_class=AlbumSerializer    