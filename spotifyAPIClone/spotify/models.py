
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.








class Artist(models.Model):
    followers=models.PositiveIntegerField()
    genres=(('P','Pop'),('H','Hip Hop'),('R','Rock'),('N','RnB'),('S','Soul'),('J','Jazz'),('C','Country'),('D','Disco'))
    name=models.CharField(max_length=155)
    genres=models.CharField(max_length=10,choices=genres,)
    popularity=models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)])
    type=models.CharField(max_length=10,default='artist')


    def __str__(self):
        return self.name

class Album(models.Model):
    name=models.CharField(max_length=90)
    release_date=models.DateField()
    type=models.CharField(max_length=20,default='Album')
    artist_list=models.ManyToManyField(Artist,related_name='artist_list')
    def __str__(self):
        return self.name



class Track(models.Model):
    albumtypes=(('A','Album'),('S','Single'),('C','Compilation'))
    albumtypes=models.CharField(max_length=1,choices=albumtypes)
    name=models.CharField(max_length=90)
    release_date=models.DateField()
    duration_ms=models.PositiveBigIntegerField()
    explicit=models.BooleanField()
    is_playable=models.BooleanField()
    popularity=models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)])
    type=models.CharField(max_length=10,default='Track')
    artists=models.ManyToManyField(Artist,related_name='artists')
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE,default=0,null=True,blank=True)
    def __str__(self):
        return self.name



