from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Profile, Summary, Category

# Serializer for the Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Serializer for the Summary model
class SummarySerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    class Meta:
        model = Summary
        fields = '__all__'

# Serializer for the Review model
class ReviewSerializer(serializers.Serializer):
    summary_id = serializers.IntegerField()
    rating = serializers.IntegerField(min_value=1, max_value=5)
    comment = serializers.CharField(max_length=200, required=False)

# Serializer for the PremiumSubscription model
class PremiumSubscriptionSerializer(serializers.Serializer):
    stripe_token = serializers.CharField()