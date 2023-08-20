from rest_framework import (
    request,
    response,
    views,
    status,
    permissions
)

from account import (
    controllers,
    permissions as account_permissions
)

from django.utils.translation import gettext as _

class RoleView(views.APIView):
    # Get Available Roles
    permission_classes = [account_permissions.RolesPermission]
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
        controllers.RoleViewController.delete_roles(request=request)
        return response.Response(
            data={
                'status_code': _('1'),
                'status_message': _('Role deleted successfully')
            },
            status=status.HTTP_200_OK
        )

class SigninView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request: request):
        profile = controllers.AccountViewController.signin(request=request)
        return response.Response(
            data={
                'status_code' : _('1'),
                'status_message' : _('Account Login successfully'),
                'data' : profile
            },
            status=status.HTTP_200_OK
        )

class SignupView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request: request):
        profile = controllers.AccountViewController.signup(request=request)
        return response.Response(
            data={
                'status_code' : _('1'),
                'status_message' : _('Account Created successfully'),
                'data' : profile
            },
            status=status.HTTP_200_OK
        )

class SignoutView(views.APIView):
    def post(self, request: request):
        controllers.AccountViewController.signout(request=request)
        return response.Response(
            data={
                'status_code' : _('1'),
                'status_message' : _('Account signout successfully')
            },
            status=status.HTTP_200_OK
        )

class ProfileView(views.APIView):
    def get(self, request: request.Request):
        profile = controllers.AccountViewController.get_profile(request=request)
        return response.Response(
            data={
                'status_code' : _('1'),
                'status_message' : _('Profile details fetched successfully'),
                'data': profile
            },
            status=status.HTTP_200_OK
        )
    def post(self, request: request.Request):
        profile = controllers.AccountViewController.update_profile(request=request)
        return response.Response(
            data={
                'status_code' : _('1'),
                'status_message' : _('Profile details updated successfully'),
                'data': profile
            },
            status=status.HTTP_200_OK
        )

class EmailVerificationView(views.APIView):
    
    permission_classes=[permissions.AllowAny]
    
    def get(self, request: request.Request):
        controllers.AccountViewController.verify_email(request=request)
        return response.Response(
            data={
                'status_code' : _('1'),
                'status_message' : _('Email verified successfully')
            },
            status=status.HTTP_200_OK
        )