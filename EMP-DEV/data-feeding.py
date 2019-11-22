>>> from social.models import *
>>> from django.contrib.auth.models import User
>>> from datetime import datetime


>>> ak_user = User.objects.get(id=1)
>>> su_user = User.objects.get(id=2)
>>> av_user = User.objects.get(id=3)
>>> sr_user = User.objects.get(id=4)


>>> ak_up_obj = UserProfile(user=ak_user, email='absalaskar@gmail.com', profile_url='www.pythonic.style/akshay', joined_on=datetime.now())
>>> ak_up_obj.save()

>>> su_up_obj = UserProfile(user=su_user, email='sunitha@gmail.com', profile_url='www.pythonic.style/sunitha', joined_on=datetime.now())
>>> su_up_obj.save()

>>> av_up_obj = UserProfile(user=av_user, email='anvesh@gmail.com', profile_url='www.pythonic.style/anvesh', joined_on=datetime.now())
>>> av_up_obj.save()

>>> sr_up_user = UserProfile(user=sr_user, email='suresh@gmail.com', profile_url='www.pythonic.style/suresh', joined_on=datetime.now())
>>> sr_up_user.save()


>>> ak_tweet = Tweet(user_profile=ak_up_obj, content='Hi, I like Python Programming Language', posted_on=datetime.now(), likes_count=50, comments_count=10, retweets_count=25)
>>> ak_tweet.save()


>>> ak_tweet = Tweet(user_profile=ak_up_obj, content='Happy Birthday Arnab', posted_on=datetime.now(), likes_count=181, comments_count=82, retweets_count=148)
>>> ak_tweet.save()


>>> su_tweet = Tweet(user_profile=su_up_obj, content='Hi, I like Dajngo Web Framework', posted_on=datetime.now(), likes_count=50, comments_count=10, retweets_count=25)
>>> su_tweet.save()


>>> av_tweet = Tweet(user_profile=av_up_obj, content='Hi, I like Flask Web Framework', posted_on=datetime.now(), likes_count=50, comments_count=10, retweets_count=25)
>>> av_tweet.save()


>>> sr_tweet = Tweet(user_profile=sr_up_obj, content='Hi, I am a Data Science Developer', posted_on=datetime.now(), likes_count=50, comments_count=10, retweets_count=25)
>>> sr_tweet.save()

>>> fr_1 = FriendRelation(from_user_profile=ak_up_obj, to_user_profile=su_up_obj, created_at=datetime.now())
>>> fr_1.save()

>>> fr_2 = FriendRelation(from_user_profile=ak_up_obj, to_user_profile=av_up_obj, created_at=datetime.now())
>>> fr_2.save()

>>> fr_3 = FriendRelation(from_user_profile=ak_up_obj, to_user_profile=sr_up_obj, created_at=datetime.now())
>>> fr_3.save()

>>> fr_4 = FriendRelation(from_user_profile=su_up_obj, to_user_profile=ak_up_obj, created_at=datetime.now())
>>> fr_4.save()

>>> fr_5 = FriendRelation(from_user_profile=av_up_obj, to_user_profile=su_up_obj, created_at=datetime.now())
>>> fr_5.save()

>>> fr_6 = FriendRelation(from_user_profile=sr_up_obj, to_user_profile=su_up_obj, created_at=datetime.now())
>>> fr_6.save()

>>> fr_7 = FriendRelation(from_user_profile=av_up_obj, to_user_profile=sr_up_obj, created_at=datetime.now())
>>> fr_7.save()

>>> fr_8 = FriendRelation(from_user_profile=sr_up_obj, to_user_profile=av_up_obj, created_at=datetime.now())
>>> fr_8.save()

>>> fr_9 = FriendRelation(from_user_profile=sr_up_obj, to_user_profile=ak_up_obj, created_at=datetime.now())
>>> fr_9.save()













