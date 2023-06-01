from django.db import models
from community.models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
# Create your models here.
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

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Summary(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    categories = models.ManyToManyField(Category, blank=True)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_cover = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    review_count = models.IntegerField(default=0, blank=True, null=True)
    # category = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Summaries"

    def __str__(self):
        return f'{self.title} - {self.author} - {self.content[:50]}'
    
    # def calculate_average_rating(self):
    #     """
    #     Calculate the average rating of the summary based on its reviews
    #     """
    #     reviews = self.rate.all()
    #     if reviews:
    #         total_reviews = len(reviews)
    #         total_ratings = sum([review.rating for review in reviews])
    #         return round(total_ratings / total_reviews, 2)
    #     else:
    #         return 0.0

    # def save(self, *args, **kwargs):
    #     self.rate = self.calculate_average_rating()
    #     self.review_count = len(self.reviews.all())
    #     super().save(*args, **kwargs)


class Subscription(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='subscription')
    is_premium = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)