from base.models import Group , Topic , Post , User
from .serializers import GroupSerializer , TopicSerializer , PostSerializer , UserSerializer
from base.api import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters , mixins , generics
from rest_framework.views import APIView


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET , POST /api/groups',
        'GET , PUT , DELETE /api/groups/:id',
        'GET , POST /api/topics',
        'GET , PUT , DELETE /api/topics/:id',
        'GET , POST /api/posts',
        'GET , PUT , DELETE /api/posts/:id',
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def GetOrAddGroups(request):
    if request.method == 'GET':
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def GroupsDealWithPK(request, pk):
    try:
        room = Group.objects.get(pk=pk)
    except Group.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = GroupSerializer(room)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        serializer = GroupSerializer(room, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        room.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


## Same Logic using Mixins
class GETorPOSTGroups(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get(self , request):
        return self.list(request)
    def post(self , request):
        return self.create(request)

class GETorPUTorDELETEGroupbyPK(mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin , generics.GenericAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get(self , request , pk):
        return self.retrieve(request)
    def put(self , request , pk):
        return self.update(request)
    def delete(self , request , pk):
        return self.destroy(request)


@api_view(['GET' , 'POST'])
def GetorAddTopics(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def TopicsDealWithPK(request, pk):
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = TopicSerializer(topic)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        serializer = TopicSerializer(topic, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        topic.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


## Same Logic using Mixins
class GETorPOSTTopics(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get(self , request):
        return self.list(request)
    def post(self , request):
        return self.create(request)


class GETorPUTorDELETETopicbyPK(mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin , generics.GenericAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get(self , request , pk):
        return self.retrieve(request)
    def put(self , request , pk):
        return self.update(request)
    def delete(self , request , pk):
        return self.destroy(request)


@api_view(['GET' , 'POST'])
def GetorAddPosts(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def PostsDealWithPK(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        post.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


## Same Logic using Mixins
class GETorPOSTPosts(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self , request):
        return self.list(request)
    def post(self , request):
        return self.create(request)


class GETorPUTorDELETEPostbyPK(mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin , generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self , request , pk):
        return self.retrieve(request)
    def put(self , request , pk):
        return self.update(request)
    def delete(self , request , pk):
        return self.destroy(request)