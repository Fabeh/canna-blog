from django.db import models
from django.utils import timezone

# Models; Start with uppercase letter.
# models.Model means that the Post is a Django Model,
# so Django knows that it should be saved in the database.

# Blog post model
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
# NOTE: This is python! Indents are necessary!
    # Method to publish the post
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # Method to return the post's title
    def __str__(self):
        return self.title
