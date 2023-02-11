from django.urls import path
from . import views

urlpatterns = [

# Products : 
# get post
path('products_mixins/', views.mixins_list.as_view()),
# get update delete
path('products_mixins/<int:pk>', views.mixins_pk.as_view()),

# Order : 
# get post
path('order_mixins/', views.mixins_list.as_view()),
# get update delete
path('order_mixins/<int:pk>', views.mixins_pk.as_view()),

# refund : 
# get post
path('refund_mixins/', views.mixins_list.as_view()),
# get update delete
path('refund_mixins/<int:pk>', views.mixins_pk.as_view()),
    
# Category : 
# get post
path('category_mixins/', views.mixins_list.as_view()),
# get update delete
path('category_mixins/<int:pk>', views.mixins_pk.as_view()),
    
]