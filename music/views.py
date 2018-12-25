'''
view with out using Generic views

# views are just python functions that takes user request & give back some respond
# a model is a blue print for how you want to store your date..
# making function to display the contain on webpage(function takes request parameter always) 
# when ever we have a view we need to return something


from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.template import loader
from .models import Album , Song


# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html') loads template file from the given path
    # when ever we pass album info into templates we pass it through dictionary 
    context = {'all_albums' : all_albums,}
    return render(request,'music/index.html/',context)#render sends httpresponse(request,templetspath,what context that templet need to work)
    # httpresponse is built in render
    
    #html = 
    #for album in all_albums:
        #url = '/music/' + str(album.id)+'/'
        #html += '<a href="' + url + '">' + album.album_title +</a><br>
    


def detail(request,album_id):
# we first query database for the id that they typed 
        #album = Album.objects.get(pk=album_id)
        album = get_object_or_404(Album, pk = album_id)
        return render(request,'music/detail.html',{'album': album })

def favorite(request,album_id):
        album = get_object_or_404(Album,pk=album_id)
        try:
                selected_song = album.song_set.get(pk=request.POST['song'] )
        except(KeyError,Song.DoesNotExist):
                return render(request,'music/detail.html',{'album':album ,
                'Error_message':'You did no select a valid song',})
        else:
                selected_song.is_favorite = True
                selected_song.save() 
                return render(request,'music/detail.html',{'album':album}) '''

'''using generic views'''

from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Album , Song

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView): # inheritate from generic ListView 
        # first specify what template we are using 
        template_name = 'music/index.html'
        context_object_name = 'all_albums'

        # query set of functions .
        def get_queryset(self):
                return Album.objects.all()


class DetailView(generic.DetailView):
        model = Album
        template_name = 'music/detail.html'

class AlbumCreate(CreateView):
        model = Album
        fields = ['artist','album_title','genres','album_logo']

class AlbumUpdate(UpdateView):
        model = Album 
        fields = ['artist','album_title','genres','album_logo']

class AlbumDelete(DeleteView):
        model = Album
        success_url = reverse_lazy('music:index')

class UserFormView(View):
        form_class = UserForm     #first specify what blue print to use for form class(UserForm) 
        template_name = 'music/registration_form.html'

        # display blank form 
        def get(self,request):
                form = self.form_class()
                return render(request,self.template_name,{'form':form})

        #process form data
        def post(self,request):
                form = self.form_class(request.POST)
                if form.is_valid():

                        user = form.save(commit=False)

                        # cleaned(normalized) data
                        username = form.cleaned_date['username']
                        password = form.cleaned_date['password']
                        user.set_password(password) # to change users password
                        user.save()

                        # return User objects if credentials are correct
                        user = authenticate(username=username,password=password)

                        if user is not None:

                                if user.is_active:
                                        login(request,user)
                                        #request.user.username to print user name
                                        return redirect('music:index')

                return render(request,self.template_name,{'form':form})
