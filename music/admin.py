from django.contrib import admin
from .models import Album,Song

# Register your models here.


# we just need to tell django album class should have admin interface
admin.site.register(Album)
admin.site.register(Song)