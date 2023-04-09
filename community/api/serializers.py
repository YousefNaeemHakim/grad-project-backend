from rest_framework import serializers
from django.contrib.auth.models import User
from community.models import Profile, Group, Post, Comment

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Serializer for the Profile model
class ProfileSerializer(serializers.ModelSerializer):
    # Nested serializer for the User model
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'avatar', 'is_premium', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    # Method to create a new Profile instance
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile

    # Method to update an existing Profile instance
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.save()
        instance.bio = validated_data.get('bio', instance.bio)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.is_premium = validated_data.get('is_premium', instance.is_premium)
        if validated_data.get('password'):
            user.set_password(validated_data['password'])
        instance.save()
        return instance

# Serializer for the Group model
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'members']

# Serializer for the Post model
class PostSerializer(serializers.ModelSerializer):
    # Nested serializer for the Profile model
    author = ProfileSerializer(read_only=True)
    # Field that returns the number of likes for a post
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'group', 'content', 'created_at', 'likes_count']

    # Method that returns the number of likes for a post
    def get_likes_count(self, obj):
        return obj.likes.count()

# Serializer for the Comment model
class CommentSerializer(serializers.ModelSerializer):
    # Nested serializer for the Profile model
    author = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'content', 'created_at']