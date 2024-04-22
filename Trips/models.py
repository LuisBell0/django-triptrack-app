from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')

    def __str__(self):
        return f'{self.city} - {self.start_date}'


class Note(models.Model):
    EXCURSION = (
        ('dinning', 'Dinning'),
        ('event', 'Event'),
        ('soccer game', 'Soccer Game'),
        ('shopping', 'Shopping'),
    )

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])
    img = models.ImageField(upload_to='notes', blank=True, null=True)   # pillow
    type = models.CharField(max_length=100, choices=EXCURSION)

    def __str__(self):
        return f'{self.name} in {self.trip.city} | rating: {self.rating}'

