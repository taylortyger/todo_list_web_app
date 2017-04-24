# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.CharField(max_length=300)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='todolist',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AddField(
            model_name='task',
            name='todolist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_list.ToDoList'),
        ),
    ]