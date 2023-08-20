from django.db import models
from django.contrib.auth import models as auth_models
# Create your models here.
class Comment(models.Model):
    message = models.CharField(
        max_length=500
    )
    commenter = models.ForeignKey(
        to=auth_models.User,
        on_delete=models.SET_NULL,
        null=True
    )
    is_resolved = models.BooleanField(
        default=False
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"
    
    def __str__(self) -> str:
        return f'{self.message}'