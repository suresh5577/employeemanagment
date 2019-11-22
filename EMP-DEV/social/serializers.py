from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['user_profile', 'content', 'posted_on', 'likes_count', 'comments_count', 'retweets_count']