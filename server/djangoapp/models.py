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
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership,
        self.name = name,
        self.purchase = purchase,
        self.review = review,
        self.purchase_date = purchase_date,
        self.car_make = car_make,
        self.car_model = car_model,
        self.car_year = car_year,
        self.sentiment = sentiment,
        self.id = id

    def __str__(self):
        return "name: " + self.name
