from django.urls import path
from . import views

urlpatterns = [

# Summary : 
# get post
path('summary_mixins/', views.mixins_list.as_view()),
# get update delete
path('summary_mixins/<int:pk>', views.mixins_pk.as_view()),

# Review : 
# get post
path('review_mixins/', views.mixins_list.as_view()),
# get update delete
path('review_mixins/<int:pk>', views.mixins_pk.as_view()),

# Category : 
# get post
path('category_mixins/', views.mixins_list.as_view()),
# get update delete
path('category_mixins/<int:pk>', views.mixins_pk.as_view()),
    
# Subscription : 
# get post
path('subscription_mixins/', views.mixins_list.as_view()),
# get update delete
path('subscription_mixins/<int:pk>', views.mixins_pk.as_view()),
    
]

