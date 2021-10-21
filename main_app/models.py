from django.db import models
from django.db.models.base import Model
from django.urls import reverse

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
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

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
        
        

