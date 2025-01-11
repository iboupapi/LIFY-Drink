from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Service(models.Model):
    class Category(models.TextChoices):
        Classique = 'CL'
        Premium = 'PM'
        GOLD = 'GD'

    name = models.fields.CharField(max_length=100)
    category = models.fields.CharField(choices=Category.choices, max_length=5)
    taille = models.fields.IntegerField()
    quantity = models.fields.IntegerField(validators= [MinValueValidator(50)])
    price = models.fields.IntegerField()
    description = models.fields.CharField(max_length=10000)
    