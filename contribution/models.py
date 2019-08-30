from django.db import models
from datetime import datetime

class Contribution(models.Model):
    user_id = models.IntegerField(blank=True)
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=False)
    post_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title

    
