from django.urls import path
from . import views


urlpatterns =[
    path("", views.home, name='home'),
    path("addtask/", views.addTask, name="addtask"),
    path("save/", views.save, name='save')
]