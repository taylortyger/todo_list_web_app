# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class ToDoList(models.Model):
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date created')
    def __str__(self):
        return self.title
        
    
class Task(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField()
    def __str__(self):
        return self.task_text
    
    class Meta:
        ordering = ["priority"]
        
    