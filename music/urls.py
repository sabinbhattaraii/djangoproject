# this is made up file so that it doesnt confuse for other urls files 
# its for making urls more orginized 
# the order of urls in urlpatterns matters 
# permissive url regex should always go later

from django.conf.urls import url
from django.urls import path,re_path # importing path function 
from . import views     # this tells the django form current directory(.) to import views 


app_name = 'music'
urlpatterns = [
    #/music/
    path('',views.IndexView.as_view(), name='index'),#'' blank because it's defult page & we have only this page to display
    # the above code basically goes to view and looks for index function

    path('register/',views.UserFormView.as_view(),name = 'register'),

    #/music/71/
    path('<int:pk>/',views.DetailView.as_view() , name = 'detail' ),
    # url looks for the view function 
    # generic views are class so views.DetailView.as_view() will convert the class into .as_view() function 


    #/music/album/add/
    path('album/add/',views.AlbumCreate.as_view(), name='album-add'),
    #/music/<album_id>/favorite
    #re_path(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite , name = 'favorite' ),

    # /music/album/2/
    path('album/<int:pk>/' ,views.AlbumUpdate.as_view(),name='album-update'),


    # /music/album/2/delete/
    path('album/<int:pk>/delete',views.AlbumDelete.as_view(),name='album-delete'),
]


'''path function takes 4 argument
        route string contaning a url pattern 
        view calls the specific view function as the pattern is matched 
        kwargs aribitrary keyword arg can be passed in a dictionary to target view
        name lets to refer to it unambiguosly for elsewhere in django '''
