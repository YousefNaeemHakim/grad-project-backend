from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes),
    path('groups/', views.GetOrAddGroups),
    path('groupss/', views.GETOrPOSTGroups.as_view()),
    path('groups/<str:pk>/', views.GroupsDealWithPK),
    path('topics/', views.GetorAddTopics),
    path('topics/<str:pk>/', views.TopicsDealWithPK),
    path('posts/', views.GetorAddPosts),
    path('posts/<str:pk>/', views.PostsDealWithPK),
]
