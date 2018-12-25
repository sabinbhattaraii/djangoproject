# a model is a blue print for database & tells how you want to store your date..
# datas like alblums songs & models is for storing those datas in the database
# make one class and django takes the class and for each variable in class it makes a table in database
# only one model for both code and database 

from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model): #every model|blueprint we create that must be inherite from models.Model 
    # inside class create varaible 
    # later on when ever we migrate table with same name 's created in database
    artist =models.CharField(max_length=250)#we always have to specify what kind of data will the varaible hold text.float
    album_title = models.CharField(max_length=500)
    genres = models.CharField(max_length =100)
    album_logo = models.FileField()

    #album_logo = models.CharField(max_length=1000)
    #when ever we create a database these above 4 columes will have but django will create another colume with unique id 
    # first Album will create id 1 and second will create id 2 and so one newid = oldid+1

    def get_absolute_url(self):
        return reverse("music:detail", kwargs={"pk": self.pk})
    
    def __str__(self): #__string__ is built in function for string representation 
        return self.artist + '--' + self.album_title 


  

class Song(models.Model): # this song should always be a part of an album ie(12 songs in 1 album)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)#foreignkey is to reference another table
# on_delete(when ever we delete any album the songs inside that will also be deleted)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default = False)

    def __str__(self):
        return self.song_title

    # foreignkey also be 1 because the song will be on album red


# primary key | unique key will de different for every colume
# foreign key is a key that establish relationship between two tables in database
# row will have unique id