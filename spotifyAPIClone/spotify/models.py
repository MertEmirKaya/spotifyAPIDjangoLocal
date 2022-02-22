
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
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
    popularity=models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)],default=50)
    artist_list=models.ManyToManyField(Artist,related_name='artist_list')
    def __str__(self):
        return self.name



class Track(models.Model):
    albumtypes=(('Album','Album'),('Album','Single'),('Album','Compilation'))
    albumtypes=models.CharField(max_length=20,choices=albumtypes)
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


class Show(models.Model):
    name=models.CharField(max_length=210,)
    description=models.TextField(null=True,blank=True)
    publisher=models.CharField(max_length=99,)
    type=models.CharField(max_length=10,default='show')
    explicit=models.BooleanField(default=True,)
    def __str__(self):
        return self.name

class Episode(models.Model):
    name=models.CharField(max_length=90)
    description=models.TextField(null=True,blank=True)
    release_date=models.DateField()
    type=models.CharField(default='show',max_length=20)
    publisher=models.CharField(max_length=75,)
    duration_ms=models.PositiveBigIntegerField()
    explicit=models.BooleanField(default=False)
    is_playable=models.BooleanField(default=True)
    language=models.CharField(max_length=5,default='en')
    


class Profil(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profil')
    ulke=[('TR','Türkiye'),('DEU','Germany'),('FR','France'),('UK','United Kingdom'),('US','United States')]
    country=models.CharField(max_length=10,choices=ulke,default='Türkiye',null=True,blank=True)
    explicit_content=models.BooleanField(default=False,null=True,blank=True)
    followers=models.PositiveIntegerField(default=0,blank=True)
    levels=[('PRE','PREMIUM'),('FREE','FREE')]
    level=models.CharField(max_length=15,choices=levels,default='FREE',blank=True)
    top_tracks=models.ManyToManyField(Track,related_name='top_tracks')
    top_artists=models.ManyToManyField(Artist,related_name='top_tracks')
    episodes=models.ManyToManyField(Episode,related_name='episodes')
    def __str__(self):
        return self.user.username




class ProfileFollowedArtists(models.Model):
    profile=models.ForeignKey(Profil,on_delete=models.PROTECT,related_name='profil',null=True)
    followed_artists=models.ManyToManyField(Artist,related_name='followed_artists')


class Playlist(models.Model):
    owner=models.ForeignKey(Profil,on_delete=models.CASCADE,related_name='owner')
    name=models.CharField(blank=True,null=True,max_length=100)
    collaborative=models.BooleanField(default=False)
    description=models.TextField(null=True,blank=True)
    followers=models.ManyToManyField(Profil,related_name='following_users')
    public=models.BooleanField(default=True)
    tracks=models.ManyToManyField(Track,related_name='tracks')
    type=models.CharField(default='playlist',max_length=10)

    def __str__(self):
        return self.name
