from django.db import models
from django.contrib.auth import models as auth_models
# Create your models here.
class Project(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True
    )
    manager = models.ForeignKey(
        to=auth_models.User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    members = models.ManyToManyField(
        to=auth_models.User,
        related_name="project_members",
        blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "projects"
    
    def __str__(self) -> str:
        return f'{self.name}'