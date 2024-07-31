from django.db import models
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to="blog/", blank=True,null=True )
    category = models.CharField(max_length=40, null=True, blank=True)
    username = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
