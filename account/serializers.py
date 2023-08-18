from rest_framework import (
    serializers
)
from rest_framework.authtoken import models as rest_models
from django.contrib.auth import models as auth_models
from account import (
    models
)
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    
    class Meta:
        model = auth_models.User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "role",
            "token",
        ]

    def get_token(self, obj):
        token, is_created = rest_models.Token.objects.get_or_create(user=obj)
        return str(token)
    
    def get_role(self, obj):
        return RoleSerializer(instance=obj.profile.role,many=False).data