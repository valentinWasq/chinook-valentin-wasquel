from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200)

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Track(models.Model):
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200, null = True)
    milliseconds = models.IntegerField(default=0)
    bytes = models.IntegerField(default=0)
    unitPrice = models.FloatField(default=0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def printDuration(self):
        return str(int(self.milliseconds / 60000)) + ':' + str(int(self.milliseconds / 1000) % 60)