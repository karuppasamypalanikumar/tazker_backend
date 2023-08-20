from django.db import models
from django.contrib.auth import models as auth_models
from project import models as project_models
# Create your models here.
class Task(models.Model):
    name = models.CharField(
        max_length=300
    )
    description = models.CharField(
        max_length=4000
    )
    assignee = models.ForeignKey(
        to=auth_models.User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assignee"
    )
    assigner = models.ForeignKey(
        to=auth_models.User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assigner"
    )
    project = models.ForeignKey(
        to=project_models.Project,
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tasks"
    
    def __str__(self) -> str:
        return f'{self.name}'