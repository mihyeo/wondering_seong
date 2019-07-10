from django.db import models
from users.models import User

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    POST_KIND_CHOICES = [
        ("card", "card"),
        ("post", "post")
    ]
    POST_CATEGORY_CHOICES = [
        ("basic", "basic"),
        ("emergency", "emergency"),
        ("news", "news")
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    kinds = models.CharField(max_length=200, choices=POST_KIND_CHOICES)
    category = models.CharField(max_length=200, choices=POST_CATEGORY_CHOICES)
    view_count = models.IntegerField(default=0)
    image = models.ImageField(null=True, upload_to="image/", blank=True)
    
    def __str__(self):
        return "{} : {}".format(self.category, self.title)    
    

class CardImage(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image/")
    
    def __str__(self):
        return "{} : {}의 이미지".format(self.pk, self.post.title)
    

class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
