from django.db import models
from django.contrib.postgres.fields import ArrayField


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=80)
    tags = ArrayField(models.CharField(max_length=100))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',)

