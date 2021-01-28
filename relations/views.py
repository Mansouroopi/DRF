
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework import viewsets
from .models import Album, Track, Student, Module
from .serializers import AlbumSerializer, StudentSerializer, ModuleSerializer, TrackSerializer

from rest_framework.response import Response


class AlbumViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class TrackViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    def create(self, *args,  **kwargs):
        """
        override the create method
        :param args:
        :param kwargs:
        :return:
        """
        track_data = self.request.data
        new_track = Track.objects.create(album=Album.objects.get(id=track_data['album']),
                                         order=track_data['order'],
                                         title=track_data['title'],
                                         duration=track_data['duration'])
        new_track.save()
        serializer = TrackSerializer(new_track)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    """
    student viewset automatically provides list, create, retrival, update, and destroy
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
