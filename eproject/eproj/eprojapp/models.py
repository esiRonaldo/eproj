from django.db import models


# Create your models here.
class Tokens(models.Model):
    name = models.CharField(max_length=255, unique=True)
    token_model = models.IntegerField(default=0)

    # machineImage = models.ImageField(upload_to='pics', default=None)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.IntegerField(format(int))
    series = models.CharField(max_length=100)
    kilometer = models.FloatField(default=0)
    price = models.FloatField(default=0)
    img = models.ImageField(upload_to='pics', default=None, null=True)

    def __str__(self):
        return self.series


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    user_token = models.ForeignKey(Tokens, on_delete=models.CASCADE)
    user_car = models.ForeignKey(Car, on_delete=models.CASCADE)

    # email=models.emailField(max_length=255)
    def __str__(self):
        return '{0} {1}'.format(self.username, self.user_token)

    class Meta:
        ordering = ["username"]
