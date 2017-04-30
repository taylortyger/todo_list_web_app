from django.conf.urls import url
from . import views

app_name = 'todo_list'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new/$', views.newList, name="new"),
    url(r'^createList/$', views.createList, name="createList"),
    url(r'^lists/(?P<list_id>[0-9]+)/$', views.manageList, name="manageList"),
    url(r'^lists/(?P<list_id>[0-9]+)/updateList/$', views.updateList, name="updateList"),
    url(r'^lists/(?P<list_id>[0-9]+)/editTitle/$', views.editTitle, name="editTitle"),
    url(r'^lists/(?P<list_id>[0-9]+)/updateTitle/$', views.updateTitle, name="updateTitle"),
    url(r'^lists/(?P<list_id>[0-9]+)/addTask/$', views.addNewTask, name="addNewTask"),
    url(r'^lists/(?P<list_id>[0-9]+)/editTask/(?P<task_id>[0-9]+)/$', views.editTask, name="editTask"),
    url(r'^lists/(?P<list_id>[0-9]+)/updateTask/(?P<task_id>[0-9]+)/$', views.updateTask, name="updateTask"),
    url(r'^lists/(?P<list_id>[0-9]+)/deleteTask/(?P<task_id>[0-9]+)/$', views.deleteTask, name="deleteTask")
]