from django.conf.urls import url
from . import views

app_name = 'todo_list'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new/$', views.newList, name="new"),
    url(r'^createList/$', views.createList, name="createList"),
    url(r'^lists/(?P<list_id>[0-9]+)/updateList/$', views.updateList, name="updateList"),
    url(r'^lists/(?P<list_id>[0-9]+)/$', views.manageList, name="manageList"),
    url(r'^lists/(?P<list_id>[0-9]+)/addTask$', views.addNewTask, name="addNewTask")
]