from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name=""),

    path('update_task/<str:pk>/', views.updateTask, name="update_task"), # update_task is the name of the URL pattern

    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"), # delete_task is the name of the URL pattern
]