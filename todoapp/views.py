from django.shortcuts import render
from .models import ToDoListItem
from django.http import HttpResponseRedirect

def todoapp_view(request):
    all_todo_items = ToDoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items': all_todo_items})

def add_todo_view(request):
    x = request.POST['content']
    new_item = ToDoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def delete_todo_view(request, i):
    y = ToDoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')