from .serializers import TrackSerializer
from spotify.models import Track
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

class TrackAPIViewSet(ModelViewSet):
    queryset=Track.objects.all()
    serializer_class=TrackSerializer