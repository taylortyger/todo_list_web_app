# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

#-------------------------------------------------------------------
#
#   To Do List Model
#
#-------------------------------------------------------------------
class ToDoList(models.Model):
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date created')
    
    def getCurrentTasks(self):
        return self.task_set.filter(completed="False")
        
    def getCompletedTasks(self):
        return self.task_set.filter(completed="True")
        
    def __str__(self):
        return self.title
        

#-------------------------------------------------------------------
#
#   Task Model, each Task belongs to a ToDoList
#
#-------------------------------------------------------------------    
class Task(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField()
    
    def __str__(self):
        return self.task_text
    
    class Meta:
        ordering = ["priority"]
        
    