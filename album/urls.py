from rest_framework import routers
from .api import AlbumViewSet

router = routers.DefaultRouter()

router.register(r'album', AlbumViewSet, 'album')

urlpatterns = router.urls