from rest_framework import serializers
from spotify.models import Track,Artist,Album


class ArtistSerializer(serializers.ModelSerializer):
     
    class Meta:
        model=Artist
        fields='__all__'   


class TrackSerializer(serializers.ModelSerializer):
    artists=serializers.StringRelatedField(many=True,)
    class Meta:
        model=Track
        fields='__all__' 


class AlbumSerializer(serializers.ModelSerializer):
    artist_list=serializers.StringRelatedField(many=True,read_only=True)
    tracks=TrackSerializer(many=True,read_only=True)
    class Meta:
        model=Album
        fields='__all__'