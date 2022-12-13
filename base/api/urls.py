from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes),
    
    # Groups Endpoins
    path('groups/', views.GetOrAddGroups),
    path('groups_mixins/', views.GETOrPOSTGroups.as_view()),
    path('groups/<str:pk>/', views.GroupsDealWithPK),
    path('groups_mixins/<str:pk>/', views.GETOrPUTOrDELETEGroupbyPK.as_view()),
    
    # Topics Endpoints
    path('topics/', views.GetOrAddTopics),
    path('topics_mixins/', views.GETOrPOSTTopics.as_view()),
    path('topics/<str:pk>/', views.TopicsDealWithPK),
    path('topics_mixins/<str:pk>/', views.GETOrPUTOrDELETETopicbyPK.as_view()),
    
    # Posts Endpoints
    path('posts/', views.GetOrAddPosts),
    path('posts_mixins/', views.GETOrPOSTPosts.as_view()),
    path('posts/<str:pk>/', views.PostsDealWithPK),
    path('posts_mixins/<str:pk>/', views.GETOrPUTOrDELETEPostbyPK.as_view()),
]
