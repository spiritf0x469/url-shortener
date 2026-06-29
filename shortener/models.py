from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shorturl(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="short_urls")
    original_url=models.URLField(max_length=100)
    short_code=models.CharField(max_length=10,unique=True)
    clicks=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)