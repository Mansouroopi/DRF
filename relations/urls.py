from django.urls import path, include
from rest_framework.routers import DefaultRouter
from relations import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'tracks', views.TrackViewSet)
router.register(r'modules', views.ModuleViewSet)
router.register(r'students', views.StudentViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]