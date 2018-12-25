from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem # we want import TodoItem from 

# Create your views here.
def todoView(request):
    #return HttpResponse('Hello This is Toview!!!')
    all_todo_items = TodoItem.objects.all()
    return render(request,'todo/todo.html',{'all_items':all_todo_items})
    # we can also edit the path in setting,py in 'DIRS':[path] also

def addTodo(request):
    c = request.POST['content']
    new_item = TodoItem(content = c)
    #create a new todo all_items
    new_item.save()
    #save
    return HttpResponseRedirect('/todo/')
    #redirect the browser to '/todo/

def deleteTodo(request,todo_id):
    item_to_delete = TodoItem.objects.get(pk = todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')