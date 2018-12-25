"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py is used for url declerations 
# table of content for the website for eg /accoutn.php 
# most of the time we give a url and it returns webpage but some time when we give url it performs task
# also does url mapping 
# url looks for the what ever pattern that matches the user request


from django.contrib import admin
from django.conf.urls import include, url 
from django.urls import path, include
"""from hello.views import myView
from todo.views import todoView,addTodo,deleteTodo"""

from django.conf import settings
from django.conf.urls.static import static 



''' for rest framework we need to import so that urls are compatible with restapi'''
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views 




urlpatterns = [ # is a list that manages info about what django should do for each url 
    path('admin/', admin.site.urls),
    path('stocks',views.StockList.as_view()),
    path('music/', include('music.urls')),
    # path(looks for the what ever pattern that matches the user request,how to respond to user request)
    #path('say/', myView),
    #path('todo/',todoView),
    #path('addTodo/', addTodo),
    #path('deleteTodo/<int:todo_id>/',deleteTodo),
]

urlpatterns = format_suffix_patterns(urlpatterns)




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root =  settings.MEDIA_ROOT)