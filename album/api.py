from .models import Album
from rest_framework import viewsets, permissions
from .serializers import AlbumSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlbumSerializer