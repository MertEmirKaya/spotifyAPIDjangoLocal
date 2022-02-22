
from .serializers import ProfilTopArtistsSerializer,TrackSerializer,ArtistSerializer,AlbumSerializer,ShowSerializer,ProfilSerializer,ProfilTopTracksSerializer,ProfileFollowedArtistsSerializer,PlaylistSerializer,EpisodeSerializer
from spotify.models import Track,Artist,Album,Show,Profil,ProfileFollowedArtists,Playlist
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

class ShowAPIViewSet(ModelViewSet):
    queryset=Show.objects.all()
    serializer_class=ShowSerializer 


class ProfilAPIViewSet(ModelViewSet):
    queryset=Profil.objects.all()
    serializer_class=ProfilSerializer 


class ProfilTopTracksListAPIView(ListAPIView):
    def get_queryset(self):
        user=self.request.user
        queryset=Profil.objects.filter(user=user)
        return queryset
    serializer_class = ProfilTopTracksSerializer 


class ProfilTopArtistsListAPIView(ListAPIView):
    def get_queryset(self):
        user=self.request.user
        queryset=Profil.objects.filter(user=user)
        return queryset
    serializer_class = ProfilTopArtistsSerializer           


class ProfileFollowedArtistsListAPIView(ListAPIView):
    def get_queryset(self):
        user=self.request.user
        queryset=ProfileFollowedArtists.objects.filter(profile=user.profil)
        return queryset    
    serializer_class = ProfileFollowedArtistsSerializer    




class PlaylistAPIViewSet(ModelViewSet):
    queryset=Playlist.objects.all()
    serializer_class = PlaylistSerializer   

class UserPlaylistsListAPIView(ListAPIView):
    def get_queryset(self):
        user=self.request.user
        queryset=Playlist.objects.filter(owner=user.profil)
        return queryset    
    serializer_class = PlaylistSerializer    




class EpisodeAPIViewSet(ModelViewSet):
    pass

