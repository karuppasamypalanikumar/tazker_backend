from rest_framework import (
    permissions
)
from django.db import (
    models
)
class RolesPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            # Apply permission logic for GET requests
            return True
        if request.user.is_authenticated:
            return True
        return False