from django.db import models
from django.utils.timezone import now


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=False, max_length=170)

    def __str__(self):
        return f'Name: {self.name}, Description: {self.description}'

class CarModel(models.Model):
    TYPE_CHOICES = [
        ('sedan', 'Sedan'), 
        ('suv', 'SUV'),
        ('wagon', 'WAGON')
    ]

    name = models.CharField(null=False, max_length=50)
    dealerid = models.IntegerField(null=False)
    carmake = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)
    type = models.CharField(null=False, max_length=50, choices=TYPE_CHOICES)
    year = models.DateField(null=False)

    def __str__(self):
        return f'Name: {self.name}'


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
