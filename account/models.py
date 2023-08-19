from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.
class Role(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    task = models.BooleanField()
    project = models.BooleanField()
    comment = models.BooleanField()

    class Meta:
        db_table = "user_roles"
    
    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(
        to=auth_models.User,
        on_delete=models.CASCADE
    )
    role = models.ForeignKey(
        to=Role,
        on_delete=models.SET_NULL,
        null=True
    )
    is_email_verified = models.BooleanField(
        default=False
    )
    is_online = models.BooleanField(
        default=False
    )
    class Meta:
        db_table = "user_profiles"
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'