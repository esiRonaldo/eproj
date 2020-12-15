from django.db import models
from django.contrib.auth.models import User
from requests import options


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    option = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snacks', 'snacks'),
    )

    name = models.CharField(max_length=50, choices=option)

    def __str__(self):
        return self.name


class Fooditem(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fats = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    calorie = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    quantity = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class UserFoodItem(models.Model):
    customer = models.ManyToManyField(Customer, blank=True)
    fooditem = models.ManyToManyField(Fooditem)
