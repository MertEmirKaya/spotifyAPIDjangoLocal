from platform import release
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

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


    def __str__(self):
        return self.name