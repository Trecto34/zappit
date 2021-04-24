from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
  title = models.CharField(max_length=100)
  url = models.URLField()
  # CASCADE is used to contain the poster name in case of account deactivation, etc.
  poster = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-created']


class Vote(models.Model):
  voter = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
