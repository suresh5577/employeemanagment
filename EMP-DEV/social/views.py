from django.shortcuts import render
from .models import * 
from .serializers import *
from rest_framework import generics, status
from django.contrib.auth.models import User 
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework import generics
from rest_framework import serializers
from rest_framework.response import Response
from datetime import datetime
from itertools import chain



class NewsFeedAPIView(APIView):
    authentication_classes = (BasicAuthentication,)


    def merge_tweets(self, news_feed, tweets):
        #merge both tweets and return only first 100
        return (sorted(chain(news_feed, tweets), key=lambda instance: instance.posted_on, reverse=True))[0:100]


    def get(self, request, format=None):
        #code as per given task
        user_profile_id = request.query_params.get('user_profile')
        user_profile = UserProfile.objects.get(id=user_profile_id)

        news_feed = []  # use this to hold final response

        # Write your code below

        friendObj = FriendRelation.objects.filter(from_user_profile = user_profile)
        friends = []
        for fr in friendObj.values('to_user_profile_id'):
            friends.append(fr['to_user_profile_id'])
        friends_tweets = Tweet.objects.filter(user_profile_id__in=friends).order_by('-posted_on')[0:100]

        owns_tweets = Tweet.objects.filter(user_profile=user_profile)

        news_feed=self.merge_tweets(owns_tweets,friends_tweets)

        serializer = TweetSerializer(news_feed, many=True)

        return  Response(serializer.data,status=status.HTTP_200_OK)



        #simple workable code without merge_tweets function for this task
        user_profile_id = request.query_params.get('user_profile')
        user_profile = UserProfile.objects.get(id=user_profile_id)
        friendObj = FriendRelation.objects.filter(from_user_profile = user_profile)
        friends = [user_profile_id]
        for fr in friendObj.values('to_user_profile_id'):
            friends.append(fr['to_user_profile_id'])
        merge_tweets = Tweet.objects.filter(user_profile_id__in=friends).order_by('-posted_on')[0:2] #you can make it [0:100] later
        serializer = TweetSerializer(merge_tweets, many=True)

        return  Response(serializer.data,status=status.HTTP_200_OK)


class TweetCreateAPIView(generics.CreateAPIView):
    authentication_classes = (BasicAuthentication,)
    """
    Complete this API when user is posting a new tweet
    """
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
        

class TimeLineListAPIView(generics.ListAPIView):
    #authentication_classes = (BasicAuthentication,)
    serializer_class = TweetSerializer

    def get_queryset(self):
        user = self.request.user
        user_profile = UserProfile.objects.get(id=user.id)
        return Tweet.objects.filter(user_profile=user_profile)
