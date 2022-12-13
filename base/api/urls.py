from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes),
    path('groups/', views.GetOrAddGroups),
    path('groups_mixins/', views.GETorPOSTGroups.as_view()),
    path('groups/<str:pk>/', views.GroupsDealWithPK),
    path('groups_mixins/<str:pk>/', views.GETorPUTorDELETEGroupbyPK.as_view()),
    path('topics/', views.GetorAddTopics),
    path('topics/<str:pk>/', views.TopicsDealWithPK),
    path('posts/', views.GetorAddPosts),
    path('posts/<str:pk>/', views.PostsDealWithPK),
]
