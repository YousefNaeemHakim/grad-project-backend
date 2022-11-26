from email import message
from pydoc_data.topics import topics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room , Topic , Message , User
from .serializers import RoomSerializer , TopicSerializer , MessageSerializer , UserSerializer
from base.api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'POST /api/room/add',
        'GET /api/topics',
        'GET /api/topics/:id',
        'POST /api/topic/add',
        'GET /api/messages',
        'GET /api/messages/:id',
        'POST /api/message/add',
        'GET /api/users',
        'GET /api/users/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addRoom(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def editRoom(request , pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room , data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['GET'])
def getTopics(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTopic(request, pk):
    topic = Topic.objects.get(id=pk)
    serializer = TopicSerializer(topic, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addTopic(request):
    serializer = TopicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['GET'])
def getMessages(request):
    message = Message.objects.all()
    serializer = MessageSerializer(message, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMessage(request , pk):
    message = Message.objects.get(id=pk)
    serializer = MessageSerializer(message, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addMessage(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = MessageSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request , pk):
    user = User.objects.get(id=pk)
    serializer = MessageSerializer(user, many=True)
    return Response(serializer.data)