from rest_framework.serializers import ModelSerializer
from base.models import Group , Topic , Post , User


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
