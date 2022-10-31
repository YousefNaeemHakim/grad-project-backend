from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),
    path('add/room/', views.addRoom),
    path('topics/', views.getTopics),
    path('topics/<str:pk>/', views.getTopic),
    path('add/topic/', views.addTopic),
    path('messages/', views.getMessages),
    path('messages/<str:pk>/', views.getMessage),
    path('add/message/', views.addMessage),
    path('users/', views.getUsers),
    path('users/<str:pk>/', views.getUser),
]
