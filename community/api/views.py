from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from community.models import Profile, Group, Post, Comment
from community.api.serializers import (GroupSerializer, PostSerializer, CommentSerializer)
import re
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/v1/',
        'GET , POST /api/v1/summaries/',
        'GET , DELETE /api/v1/summaries/<id>/',
        'POST /api/v1/summary/<int:pk>/review/',
        'POST /api/v1/group/',
        'DELETE /api/v1/group/<int:pk>/',
        'PATCH /api/v1/group/<int:pk>/join/',
        'PATCH /api/v1/group/<int:pk>/leave/',
        'PATCH /api/v1/post/<int:pk>/like/',
        'POST /api/v1/post/<int:pk>/comment/',
        'DELETE /api/v1/posts/comments/<int:pk>/',
        'POST /api/v1/post/create/',
        'PUT , PATCH /api/v1/post/<int:pk>/update/',
        'DELETE /api/v1/post/<int:pk>/delete/',
        'GET , POST /api/v1/roadmaps/',
        'GET , PUT , PATCH , DELETE /api/v1/roadmaps/<int:pk>/',
        'POST /api/v1/roadmaps/<int:pk>/steps/',
        'GET , PUT , PATCH , DELETE /api/v1/steps/<int:pk>/',
    ]
    return Response(routes)

# View for creating a new group
class GroupCreateView(generics.CreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class GroupSearchView(generics.ListAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Group.objects.all()
        search_query = self.request.query_params.get('q', None)
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query))
        return queryset

# View for destroying a group
class GroupDestroyView(generics.DestroyAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated]
    
    # Delete the group if the user who requested the deletion is the group's owner
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied
        return self.destroy(request, *args, **kwargs)


# View for joining a group
class GroupJoinView(generics.UpdateAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated]

     # Add the requesting user to the group's members list if they are not already a member
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.profile in instance.members.all():
            return Response({'message': 'User already a member'}, status=status.HTTP_400_BAD_REQUEST)
        instance.members.add(request.user.profile)
        return Response(status=status.HTTP_204_NO_CONTENT)


# View for leaving a group
class GroupLeaveView(generics.UpdateAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated]

    # Remove the requesting user from the group's members list if they are a member
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.profile not in instance.members.all():
            return Response({'message': 'User not a member'}, status=status.HTTP_400_BAD_REQUEST)
        instance.members.remove(request.user.profile)
        return Response(status=status.HTTP_204_NO_CONTENT)


# View for liking a post
class PostLikeView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    # Toggle the requesting user's like status on the post
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.profile in instance.likes.all():
            instance.likes.remove(request.user.profile)
        else:
            instance.likes.add(request.user.profile)
        return Response(status=status.HTTP_204_NO_CONTENT)


# View for commenting on a post
class PostCommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

     # Save the user who created the comment
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# View for creating a new post
class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # Save the user who created the post
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# View for updating a post
class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied
        return super().update(request, *args, **kwargs)


class PostDestroyView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied
        return self.destroy(request, *args, **kwargs)


class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()

        # Check if the user is the owner of the comment or a moderator
        if comment.user != request.user and not request.user.is_staff:
            return Response({"detail": "You do not have permission to delete this comment."}, status=status.HTTP_403_FORBIDDEN)

        comment.delete()
        return Response({"detail": "Comment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)