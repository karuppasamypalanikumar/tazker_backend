from rest_framework import (
    serializers
)

from . import (
    models as project_models
)

from django.contrib.auth import (
    models as auth_models
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth_models.User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email'
        ]

class ProjectSerializer(serializers.ModelSerializer):
    manager = UserSerializer(many=False)
    members = UserSerializer(many=True)
    class Meta:
        model = project_models.Project
        fields = [
            'id',
            'name',
            'manager',
            'members',
            'created_on',
            'updated_on'
        ]
