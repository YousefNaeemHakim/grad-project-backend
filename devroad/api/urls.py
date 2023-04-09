from django.urls import path
from devroad.api.views import (RoadmapList, RoadmapDetail, RoadmapSearch, RoadmapStepDetail, RoadmapStepList)


urlpatterns = [
    path('roadmaps/', RoadmapList.as_view(), name='roadmap-list'),  # URL for RoadmapList view
    path('roadmap/search/', RoadmapSearch.as_view(), name='roadmap-search'),
    path('roadmaps/<uuid:id>/', RoadmapDetail.as_view(), name='roadmap-detail'),  # URL for RoadmapDetail view
    path('steps/<uuid:id>/', RoadmapStepDetail.as_view(), name='step-detail'),  # URL for StepDetail view
    path('roadmaps/<int:roadmap_id>/steps/', RoadmapStepList.as_view(), name='roadmap-step-list'),  # URL for RoadmapStepList view
    # path('steps/', RoadmapStepList.as_view(), name='step-list'),  # URL for StepList view
    # path('subscription/', SubscriptionView.as_view()),
]