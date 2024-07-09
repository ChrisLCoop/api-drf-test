from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import Album

class AlbumFilter(filters.FilterSet):
    class Meta:
        model = Album
        fields = ['titulo','categoria']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id','titulo','descripcion','categoria','img_portada','url_music_download')
        #fields = '__all__'
        filterset_class = AlbumFilter