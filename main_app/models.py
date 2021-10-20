from django.db import models

# Create your models here.
# Add the Finch class & list and view function below the imports
class Finch: # Note that parens are optional if not inheriting from another class
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

finches = [
    Finch('Groot', 'American Goldfinch', 'demon bird', 4),
    Finch('Lexi', 'Common Redpoll', 'nice bird', 3),
    Finch('Loki', 'Indigo Bunting', 'crazy bird', 5),
]