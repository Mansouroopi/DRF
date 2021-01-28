from django.db import models


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.SET_NULL, null=True)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __unicode__(self):
        """
        RelatedField may be used to represent the target of the relationship using its __unicode__ method.
        :return:
        """
        return '%d: %s' % (self.order, self.title)


class Module(models.Model):
    name = models.CharField(max_length=200)
    length = models.IntegerField()
    class_room = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    grade = models.IntegerField()
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return self.name
