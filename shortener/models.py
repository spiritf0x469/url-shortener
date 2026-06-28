from django.db import models

# Create your models here.
class Shorturl(models.Model):
    original_url=models.URLField(max_length=100)
    short_code=models.CharField(max_length=10,unique=True)
    clicks=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)