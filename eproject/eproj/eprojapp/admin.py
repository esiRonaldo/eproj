from django.contrib import admin
from .models import User, Tokens, Car

# Register your models here.
admin.site.register(Tokens)
admin.site.register(User)
admin.site.register(Car)
