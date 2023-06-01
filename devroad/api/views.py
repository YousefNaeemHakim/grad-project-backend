from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from devroad.models import Roadmap, RoadmapStep
from devroad.api.serializers import (RoadmapSerializer, RoadmapStepSerializer)
import re

class RoadmapList(generics.ListCreateAPIView):
    queryset = Roadmap.objects.all()  # Specify queryset for GET (list) and POST operations
    serializer_class = RoadmapSerializer  # Specify serializer class for GET and POST operations


class RoadmapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roadmap.objects.all()  # Specify queryset for GET (detail), PUT, and DELETE operations
    serializer_class = RoadmapSerializer  # Specify serializer class for GET (detail), PUT, and DELETE operations

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(self.object)

        # Retrieve titles of all steps associated with the roadmap
        steps = RoadmapStep.objects.filter(roadmap=self.object)
        step_titles = [step.title for step in steps]

        # Add step_titles to the serialized data
        serialized_data = serializer.data
        serialized_data['step_titles'] = step_titles

        return Response(serialized_data)


class RoadmapSearch(generics.ListAPIView):
    serializer_class = RoadmapSerializer

    def get_queryset(self):
        queryset = Roadmap.objects.all()
        search_query = self.request.query_params.get('q', None)
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))
        return queryset


class RoadmapStepList(generics.ListCreateAPIView):
    queryset = RoadmapStep.objects.all()  # Specify queryset for GET (list) and POST operations
    serializer_class = RoadmapStepSerializer  # Specify serializer class for GET and POST operations


class RoadmapStepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoadmapStep.objects.all()  # Specify queryset for GET (detail), PUT, and DELETE operations
    serializer_class = RoadmapStepSerializer  # Specify serializer class for GET (detail), PUT, and DELETE operations


class RoadmapStepList(generics.ListCreateAPIView):
    serializer_class = RoadmapStepSerializer

    def get_queryset(self):
        roadmap_id = self.kwargs['roadmap_id']
        return RoadmapStep.objects.filter(roadmap_id=roadmap_id)

    def create(self, request, *args, **kwargs):
        roadmap_id = self.kwargs['roadmap_id']
        roadmap = Roadmap.objects.filter(id=roadmap_id).first()

        if roadmap is None:
            return Response({'error': 'Roadmap not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(roadmap=roadmap)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RoadmapStepSearch(generics.ListAPIView):
    serializer_class = RoadmapStepSerializer

    def get_queryset(self):
        queryset = RoadmapStep.objects.all()
        search_query = self.request.query_params.get('q', None)
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(roadmap__icontains=search_query))