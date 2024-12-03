from django.db import models

# Create your models here.

class Project(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField()
   technology = models.CharField(max_length=200)
   image = models.ImageField(upload_to='projects/')
   github_url = models.URLField(blank=True)
   live_url = models.URLField(blank=True)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.title

   class Meta:
       ordering = ['-created_at']