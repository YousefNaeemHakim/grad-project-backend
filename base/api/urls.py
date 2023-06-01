from django.urls import path
from base.api.views import (SummaryList, SummaryDetail, SummarySearch, SummaryReviewView,
                    CategoryListCreateView, CategoryRetrieveUpdateDestroyView)


urlpatterns = [
    path('summaries/', SummaryList.as_view()),
    path('summaries/<uuid:id>', SummaryDetail.as_view()),
    path('summaries/search/', SummarySearch.as_view(), name='summary-search'),
    path('summary/<uuid:id>/review/', SummaryReviewView.as_view()),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<uuid:id>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),
]