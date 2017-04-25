# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from .models import ToDoList

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
    
def updateList(request):
    return HttpResponse("hi")

