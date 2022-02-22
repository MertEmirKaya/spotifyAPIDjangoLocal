from rest_framework import serializers
from spotify.models import Track,Artist,Album,Show,Profil,ProfileFollowedArtists,Playlist,Episode


class ArtistSerializer(serializers.ModelSerializer):
     
    class Meta:
        model=Artist
        fields='__all__'   


class TrackSerializer(serializers.ModelSerializer):
    artists=serializers.StringRelatedField(many=True,)
    album=serializers.StringRelatedField()
    class Meta:
        model=Track
        fields='__all__' 


class AlbumSerializer(serializers.ModelSerializer):
    artist_list=serializers.StringRelatedField(many=True,read_only=True)
    tracks=TrackSerializer(many=True,read_only=True)
    class Meta:
        model=Album
        fields='__all__'


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model=Show
        fields='__all__'            

class ProfilSerializer(serializers.ModelSerializer):
    top_tracks=serializers.StringRelatedField(many=True,read_only=True)
    user=serializers.StringRelatedField()
    class Meta:
        model=Profil
        fields='__all__' 

class ProfilTopTracksSerializer(serializers.ModelSerializer):
    top_tracks=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=Profil
        fields=['top_tracks']


class ProfilTopArtistsSerializer(serializers.ModelSerializer):
    top_artists=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=Profil
        fields=['top_artists']                          


class ProfileFollowedArtistsSerializer(serializers.ModelSerializer):
    followed_artists=serializers.StringRelatedField(many=True,)
    class Meta:
        model=ProfileFollowedArtists
        fields=['followed_artists']


class PlaylistSerializer(serializers.ModelSerializer):
    followers=serializers.StringRelatedField(many=True)
    tracks=serializers.StringRelatedField(many=True)
    class Meta:
        model=Playlist
        fields='__all__'        

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Episode
        fields='__all__'      