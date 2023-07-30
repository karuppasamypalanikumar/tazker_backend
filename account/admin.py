from django.contrib import admin
from account import models

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Role)