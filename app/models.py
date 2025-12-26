from django.db import models

# Create your models here.
class School(models.Model):
    scname=models.CharField()
    scloc=models.CharField()
    scid=models.IntegerField()


    def __str__(self):
        return self.scname