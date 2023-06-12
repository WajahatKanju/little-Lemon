from django.db import models

# Create your models here.


class Booking(models.Model):

    name = models.CharField('Name', max_length=255)
    no_of_guests = models.SmallIntegerField('Number of guests')
    booking_date = models.DateTimeField('Booking date')


class Menu(models.Model):

    title = models.CharField('Dish Name', max_length=255)
    price = models.DecimalField('Dish Price', max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField('Dish Inventory')

    # add the following method in Menu class
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
