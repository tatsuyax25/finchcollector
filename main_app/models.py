from django.db import models
from django.urls import reverse

# Create your models here.
# Add the Finch class & list and view function below the imports
class Finch(models.Model): # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    age = models.IntegerField() 
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})


        

