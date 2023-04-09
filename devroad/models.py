from django.db import models
import uuid
# Create your models here.


class Roadmap(models.Model):    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    
    @property
    def steps(self):
        return ', '.join(self.roadmapstep_set.values_list('title', flat=True))

    def __str__(self):
        return f'{self.title}'

class RoadmapStep(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=200,blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.title} ({self.roadmap.title})'