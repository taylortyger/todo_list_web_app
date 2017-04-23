from django.conf.urls import url
from . import views

app_name = 'todo_list'

urlpatterns = [
    url(r'^$', views.index, name="index")
]