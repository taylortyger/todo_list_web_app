# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from .models import ToDoList, Task

#---------------------------------------------------------
#
#   Homepage of To Do List app
#
#---------------------------------------------------------
def index(request):
    return render(request, 'todo_list/index.html', {})

#---------------------------------------------------------
#
#   View for starting a new to do list.
#
#---------------------------------------------------------
def newList(request):
    return render(request, 'todo_list/newList.html', {})

#-------------------------------------------------------------------------------
#
#   Creates a new to do list in the database based on information sent from 
#   newList view.
#
#-------------------------------------------------------------------------------
def createList(request):
    listTitle = request.POST['list_title']
    
    #validate Title
    if(listTitle != ""):
        l = ToDoList(title=listTitle, pub_date=timezone.now())
        l.save()
        return HttpResponseRedirect(reverse('todo_list:manageList', args=(l.id,)))
    
    #Title was invalid
    else:
        return render(request, 'todo_list/newList.html', {
            'error_message': "Invalid Title.",
        })

#-------------------------------------------------------------------
#
#   Page for viewing, editing, and interacting with a to do list
#
#------------------------------------------------------------------- 
def manageList(request, list_id):
    todoList = get_object_or_404(ToDoList, pk=list_id)
    return render(request, 'todo_list/manageList.html', {'todoList': todoList})

#-------------------------------------------------------------------
#
#   Marks tasks as completed based on POST data sent from manageList
#
#------------------------------------------------------------------- 
def updateList(request, list_id):
    todoList = get_object_or_404(ToDoList, pk=list_id)
    
    # mark newly completed tasks as complete in the database
    completedTasks = request.POST.getlist('task_completed')
    numErrors = 0
    for taskID in completedTasks:
        try:
            currentTask = todoList.task_set.get(pk=taskID)
        except (KeyError, Task.DoesNotExist):
            numErrors += 1
        else:
            currentTask.completed=True
            currentTask.save()
    return HttpResponseRedirect(reverse('todo_list:manageList', args=(todoList.id,)))
    
#-------------------------------------------------------------------
#
#   Add's a new task to the to do list based on POST request from 
#   manage list view. 
#
#-------------------------------------------------------------------
def addNewTask(request, list_id):
    todoList = get_object_or_404(ToDoList, pk=list_id)
    newTask_text = request.POST['newtask_text']
    newTask_priority = request.POST['newtask_priority']
    
    if(newTask_priority == ""):
        newTask_priority = 0
    if(newTask_text != ""):
        todoList.task_set.create(task_text=newTask_text, priority=newTask_priority)
        return HttpResponseRedirect(reverse('todo_list:manageList', args=(todoList.id,)))
    
    # task text was invalid (empty)
    else:
        return render(request, 'todo_list/manageList.html', {
            'error_message': "Invalid Task Text.",
            'todoList': todoList
        })
