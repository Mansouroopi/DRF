from rest_framework import serializers
from .models import Album, Track, Module, Student


class AlbumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Album
        fields = ('album_name', 'artist')


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ('order', 'title', 'duration', 'album', 'album')
        depth = 1


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = ['name', 'length', 'class_room']


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'age', 'grade', 'modules']
        depth = 1
