from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    area = models.CharField(max_length=200)
    adminUser = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    postcode = models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
    