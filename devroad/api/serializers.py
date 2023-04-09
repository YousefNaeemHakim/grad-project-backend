from rest_framework import serializers
from django.contrib.auth.models import User
from devroad.models import Roadmap, RoadmapStep


class RoadmapStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadmapStep
        fields = ('id', 'title', 'description', 'order' , 'content')


class RoadmapSerializer(serializers.ModelSerializer):
    steps = RoadmapStepSerializer(many=True, read_only=True)

    class Meta:
        model = Roadmap
        fields = ('id', 'title', 'description', 'steps')