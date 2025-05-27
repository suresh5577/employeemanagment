from django.urls import path
from . import views


urlpatterns = [
    path('get_news_feed/', views.NewsFeedAPIView.as_view(), name='get_news_feed'),
    path('create_tweet/', views.TweetCreateAPIView.as_view(), name='create_tweet'),
    path('own_tweets/', views.TimeLineListAPIView.as_view(), name='own_tweets'),
]