from django.db import models
# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    description = models.TextField()
    number = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.email}"

    
