from rest_framework import (
    request,
    response,
    views,
    status
)

from account import (
    controllers
)

from django.utils.translation import gettext as _

class RoleView(views.APIView):
    # Get Available Roles
    def get(self, request: request.Request):
        roles = controllers.RoleViewController.get_roles(request=request)
        return response.Response(
            data={
                'status_code' : _('1'),
                'status_message' : _('Data fetched successfully'),
                'data' : roles
            },
            status=status.HTTP_200_OK
        )
    # Create New Roles
    def post(self, request: request.Request):
        role = controllers.RoleViewController.create_role(request=request)
        return response.Response(
            data={
                'status_code': _('1'),
                'status_message': _('Role created successfully'),
                'data': role
            },
            status=status.HTTP_200_OK
        )
    # Update Existing Roles
    def put(self, request: request.Request):
        role = controllers.RoleViewController.update_role(request=request)
        return response.Response(
            data={
                'status_code': _('1'),
                'status_message': _('Role updated successfully'),
                'data': role
            },
            status=status.HTTP_200_OK
        )
    # Delete Existing Roles
    def delete(self, request: request.Request):
        controllers.RoleViewController.delete_role(request=request)
        return response.Response(
            data={
                'status_code': _('1'),
                'status_message': _('Role deleted successfully')
            },
            status=status.HTTP_200_OK
        )