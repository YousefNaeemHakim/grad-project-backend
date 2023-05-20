from django.db import models
from django.db.models import Avg
from community.models import Profile
import uuid

class Summary(models.Model):
     Rate = models.DecimalField(decimal_places=2, max_digits=3)
     def calculate_average_rating():
      average_rating = Summary.objects.aggregate(Avg('rating'))['rating__avg']
      return average_rating

     created_at= models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     title = models.CharField(max_length=100)
     content = models.TextField()
     author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    


class Review(models.Model): 
     title = models.CharField(max_length=100)
     content = models.TextField()
     rating = models.DecimalField(decimal_places=2, max_digits=3)
     user = models.ForeignKey(Profile, on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    class CategoryTypes(models.TextChoices):
        SCIENCE = 'Science'
        HISTORY = 'History'
        RELIGIONS = 'Religions'
        POLITICS = 'Politics'
        PSYCHOLOGY = 'Psychology'
        PHILOSOPHY = 'Philosophy'
        ISLAMIC_SCIENCES = 'Islamic Sciences'
        PERSONAL_GROWTH = 'Personal Growth'
        BUSINESS = 'Business'
        TECHNOLOGY = 'Technology'
        COMPUTER_SCIENCE = 'Computer Science'
        SOFTWARE_ENGINEERING = 'Software Engineering'
        MOBILE_DEV = 'Mobile Development'
        WEB_DEV = 'Web Development'
        CODING_INTERVIEWS = 'Coding Interviews'

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=20, choices=CategoryTypes.choices)
    description = models.TextField(blank=True, null=True) 

class Subscription(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
