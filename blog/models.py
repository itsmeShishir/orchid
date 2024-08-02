from django.db import models
from category.models import Category


class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to="blog/", blank=True,null=True )
    category = models.ForeignKey(Category,
                                 blank=True, 
                                 null=True, 
                                 on_delete=models.CASCADE,)
    username = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
    

