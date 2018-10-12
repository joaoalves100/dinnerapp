from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Meals(models.Model):
    meal_date = models.DateTimeField('meal date')
    meal_description = models.CharField(max_length = 300)


class People(models.Model):
    name= models.CharField(max_length=200)
    house_guest = models.BooleanField()
    phone_number = models.CharField(max_length = 20)

class Participation(models.Model):
    meal = models.ForeignKey(Meals, on_delete = models.CASCADE)
    people =models.ForeignKey(People, on_delete = models.CASCADE)
    number_guests = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],)
    creation_time = models.DateTimeField(auto_now_add=True)
