from rest_framework import (
    serializers
)
from account import (
    models
)
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = "__all__"