from django.db import models
from django.contrib.auth.models import User 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=120)
    profile_url = models.URLField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

class Tweet(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='user_tweets', on_delete=models.CASCADE)
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    retweets_count = models.IntegerField(default=0)

class FriendRelation(models.Model):
    from_user_profile = models.ForeignKey(UserProfile, related_name='user_followings', on_delete=models.CASCADE)
    to_user_profile = models.ForeignKey(UserProfile, related_name='user_followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
