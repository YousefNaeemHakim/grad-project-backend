from django.urls import path
from . import views

urlpatterns = [

# Summary : 
# get post
path('summary/', views.mixins_list.as_view()), 
# get update delete
path('summary/<int:pk>', views.mixins_pk.as_view()),

# Review : 
# get post
path('review/', views.mixins_list.as_view()),
# get update delete
path('review/<int:pk>', views.mixins_pk.as_view()),

# Category : 
# get post
path('category/', views.mixins_list.as_view()),
# get update delete
path('category/<int:pk>', views.mixins_pk.as_view()),
    
# Subscription : 
# get post
path('subscription/', views.mixins_list.as_view()),
# get update delete
path('subscription/<int:pk>', views.mixins_pk.as_view()),
    
]

