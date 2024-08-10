from django.utils import timezone
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ["date_posted"]
    
    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)
    