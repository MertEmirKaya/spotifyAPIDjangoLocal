from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TrackAPIViewSet
route=DefaultRouter()
route.register(r'tracks',TrackAPIViewSet)

urlpatterns = [
    path('',include(route.urls)),
]