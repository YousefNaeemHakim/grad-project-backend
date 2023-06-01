from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from base.models import Profile, Summary, Category
from base.api.serializers import (SummarySerializer,CategorySerializer ,ReviewSerializer)
import re

# GET /summaries/: Get all summaries
# POST /summaries/: Create a new summary
class SummaryList(generics.ListCreateAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer

# GET /summaries/<id>/: Get a specific summary by ID
# DELETE /summaries/<id>/: Delete a specific summary by ID
class SummaryDetail(generics.RetrieveDestroyAPIView):
    serializer_class = SummarySerializer

    def get_queryset(self):
        return Summary.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()

        # Check if the 'id' parameter is in the URL
        summary_id = self.kwargs.get('id')
        if summary_id:
            obj = get_object_or_404(queryset, id=summary_id)
            self.check_object_permissions(self.request, obj)
            return obj

        # Check if the 'title' parameter is in the URL
        summary_title = self.kwargs.get('title')
        if summary_title:
            # Use regex search to find summaries with titles that match the given string
            matching_summaries = [summary for summary in queryset if re.search(summary_title, summary.title, re.IGNORECASE)]
            
            if len(matching_summaries) == 0:
                raise Http404
            elif len(matching_summaries) == 1:
                obj = matching_summaries[0]
            else:
                # If multiple matching summaries are found, return the first one
                obj = matching_summaries[:5]

            self.check_object_permissions(self.request, obj)
            return obj

        # Return a 404 response if neither 'id' nor 'title' is in the URL
        raise Http404

class SummarySearch(generics.ListAPIView):
    serializer_class = SummarySerializer

    def get_queryset(self):
        queryset = Summary.objects.all()
        search_query = self.request.query_params.get('q', None)
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query) | Q(categories__icontains=search_query))
        return queryset

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'title'
    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned queryset by filtering against
        a `name` query parameter in the URL.
        """
        queryset = Category.objects.all()
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

# View for creating summary review
class SummaryReviewView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    # Save the user who created the summary review
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# View for creating summary review برضو
class CreateReview(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        summary_id = kwargs.get('summary_id')
        summary = Summary.objects.get(id=summary_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(summary=summary, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)