from rest_framework import serializers
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id','titulo','descripcion','categoria','img_portada','url_music_download')
        #fields = '__all__'