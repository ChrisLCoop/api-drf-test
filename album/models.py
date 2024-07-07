from django.db import models

# Create your models here.

class Album(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=250)
    categoria = models.CharField(max_length=30)
    img_portada = models.CharField(max_length=255)
    url_music_download = models.CharField(max_length=255,default="null")
