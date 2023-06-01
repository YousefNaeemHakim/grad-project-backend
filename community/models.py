from django.db import models
from django.contrib.auth.models import User
import uuid
from django_countries.fields import CountryField


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    country = CountryField(blank=True, null=True, default=None, blank_label=" Select Country ")
    language = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    facebookLink = models.URLField(blank=True, null=True)
    twitterLink = models.URLField(blank=True, null=True)
    linkedInLink = models.URLField(blank=True, null=True)
    # Add more social links attributes here as needed

    def __str__(self):
        return self.user.username


class Group(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Profile, related_name='groups')

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(Profile, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} commented on {self.post.title}'
