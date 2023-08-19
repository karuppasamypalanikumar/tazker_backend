from rest_framework import (
    request,
    serializers,
    status
)
from django.db import models as django_models
from django.contrib.auth import models as auth_models
from account import (
    models as account_models,
    serializers as account_serializers
)
from helpers import validator
from django.utils.translation import gettext as _

class RoleViewController():
    
    @staticmethod
    def get_roles(request: request.Request):
        data = account_models.Role.objects.all()
        roles = account_serializers.RoleSerializer(
            instance=data,
            many=True
        ).data
        return roles
    
    @staticmethod
    def create_role(request: request.Request):
        name = validator.check(
            key="name",
            type=validator.AvailableTypes.String,
            request=request,
            max_count=100
        )
        project = validator.check(
            key="project",
            type=validator.AvailableTypes.Boolean,
            request=request
        )
        task = validator.check(
            key="task",
            type=validator.AvailableTypes.Boolean,
            request=request
        )
        comment = validator.check(
            key="comment",
            type=validator.AvailableTypes.Boolean,
            request=request
        )
        # create Role
        try:
            role = account_models.Role.objects.create(
                name=name,
                project=project,
                task=task,
                comment=comment
            )
        except Exception as e:
            raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _(f'Create Role Failed with error: {str(e)}')
                },
                code=status.HTTP_400_BAD_REQUEST
            )
        role_data = account_serializers.RoleSerializer(
            instance=role,
            many=False
        ).data
        return role_data
    
    @staticmethod
    def update_role(request: request.Request):
         # update Role
        id = validator.check(
            key="id",
            type=validator.AvailableTypes.Integer,
            request=request
        )
        name = request.data.get("name")
        task = request.data.get("task")
        comment = request.data.get("comment")
        project = request.data.get("project")
        try:
            role = account_models.Role.objects.get(id=id)
            if name:
                name = validator.check(
                    key="name",
                    type=validator.AvailableTypes.String,
                    request=request
                )
                role.name = name
            if task is not None:
                task = validator.check(
                    key="task",
                    type=validator.AvailableTypes.Boolean,
                    request=request
                )
                role.task = task
            if comment is not None:
                comment = validator.check(
                    key="comment",
                    type=validator.AvailableTypes.Boolean,
                    request=request
                )
                role.comment = comment
            if project is not None:
                project = validator.check(
                    key="project",
                    type=validator.AvailableTypes.Boolean,
                    request=request
                )
                role.project = project
            role.save()
        except account_models.Role.DoesNotExist:
            raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _('Invalid role id')
                },
                code=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _(f'Update Role Failed with error: {str(e)}')
                },
                code=status.HTTP_400_BAD_REQUEST
            )
        role_data = account_serializers.RoleSerializer(
            instance=role,
            many=False
        ).data
        return role_data
    
    @staticmethod
    def delete_role(request: request.Request):
        # Delete Role
        id = validator.check(
            key="id",
            type=validator.AvailableTypes.String,
            request=request
        )
        try:
            role = account_models.Role.objects.get(id=id)
            role.delete()
        except account_models.Role.DoesNotExist:
            raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _('Invalid role id')
                },
                code=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _(f'Delete Role Failed with error: {str(e)}')
                },
                code=status.HTTP_400_BAD_REQUEST
            )

class AccountViewController():
    
    @staticmethod
    def signin(request: request.Request):
        username_or_email = validator.check(
            key="username",
            type=validator.AvailableTypes.String,
            request=request
        )
        password = validator.check(
            key="password",
            type=validator.AvailableTypes.String,
            request=request
        )
        try:
            user = auth_models.User.objects.get(
                django_models.Q(username=username_or_email) |
                django_models.Q(email=username_or_email)
            )
        except auth_models.User.DoesNotExist:
            raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _('no user found')
                },
                code=status.HTTP_400_BAD_REQUEST
            )
        if user:
            # Verify the password
            if user.password != password:
                raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _('Invalid password')
                },
                code=status.HTTP_400_BAD_REQUEST
            )
            profile = user.profile
            profile.is_online=True
            profile.save()
            data = account_serializers.ProfileSerializer(
                instance=user,
                many=False
            ).data
            return data
                
    
    @staticmethod
    def signup(request: request.Request):
        username = validator.check(
            key="username",
            type=validator.AvailableTypes.String,
            request=request,
            max_count=150
        )
        first_name = validator.check(
            key="first_name",
            type=validator.AvailableTypes.String,
            request=request,
            max_count=150
        )
        last_name = validator.check(
            key="last_name",
            type=validator.AvailableTypes.String,
            request=request,
            max_count=150
        )
        email = validator.check(
            key="email",
            type=validator.AvailableTypes.String,
            request=request,
            max_count=254,
            is_email=True
        )
        # check email already exist
        if auth_models.User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _('email already exist')
                },
                code=status.HTTP_400_BAD_REQUEST
            )
        password = validator.check(
            key="password",
            type=validator.AvailableTypes.String,
            request=request,
            max_count=128,
            is_password=True
        )
        confirm_password = validator.check(
            key="confirm_password",
            type=validator.AvailableTypes.String,
            request=request,
            max_count=128,
            is_password=True
        )
        role_id = validator.check(
            key="role_id",
            type=validator.AvailableTypes.Integer,
            request=request
        )
        if password != confirm_password:
            raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _('password and confirm_password mismatch')
                },
                code=status.HTTP_400_BAD_REQUEST
            )
        try:
            role = account_models.Role.objects.get(
                id=role_id
            )
            user = auth_models.User.objects.create(
                password=password,
                is_superuser=False,
                username=username,
                last_name=last_name,
                email=email,
                is_active=True,
                first_name=first_name
            )
            profile = account_models.Profile.objects.create(
                user=user,
                role=role
            )
            profile.is_online=True
            profile.save()
            result_data = account_serializers.ProfileSerializer(
                instance=user,
                many=False
            ).data
            return result_data
        except account_models.Role.DoesNotExist:
            raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _(f'invalid role id')
                },
                code=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _(f'user creation failed with {str(e)}')
                },
                code=status.HTTP_400_BAD_REQUEST
            )

    @staticmethod
    def signout(request: request.Request):
        user = request.user
        profile = user.profile
        profile.is_online=False
        profile.save()
    
    @staticmethod
    def get_profile(request: request.Request):
        user = request.user
        result_data = account_serializers.ProfileSerializer(
            instance=user,
            many=False
        ).data
        return result_data

    @staticmethod
    def update_profile(request: request.Request):
        data = request.data
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        role_id = data.get('role_id')
        user = request.user
        profile = user.profile
        if username:
            username = validator.check(
                key="username",
                type=validator.AvailableTypes.String,
                request=request,
                max_count=150
            )
            try:
                user.username = username
                user.save()
            except Exception as e:
                raise serializers.ValidationError(
                    detail={
                        'status_code': _('0'),
                        'status_message': _(f'username is not available please pick another one')
                    },
                    code=status.HTTP_400_BAD_REQUEST
                )
        if first_name:
            first_name = validator.check(
                key="first_name",
                type=validator.AvailableTypes.String,
                request=request,
                max_count=150
            )
            user.first_name = first_name
        if last_name:
            last_name = validator.check(
                key="last_name",
                type=validator.AvailableTypes.String,
                request=request,
                max_count=150
            )
            user.last_name = last_name
        if email:
            email = validator.check(
                key="email",
                type=validator.AvailableTypes.String,
                request=request,
                max_count=254,
                is_email=True
            )
            user.email = email
            profile.is_email_verified = False
        if role_id:
            role_id = validator.check(
                key="role_id",
                type=validator.AvailableTypes.Integer,
                request=request
            )
            try:
                role = account_models.Role.objects.get(
                    id=role_id
                )
                profile.role = role
            except account_models.Role.DoesNotExist:
                 raise serializers.ValidationError(
                    detail={
                        'status_code': _('0'),
                        'status_message': _(f'invalid role id')
                    },
                    code=status.HTTP_400_BAD_REQUEST
                )
        try:
            user.save()
            profile.save()
            result_data = account_serializers.ProfileSerializer(
                instance=user,
                many=False
            ).data
            return result_data
        except ValueError:
            raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _(f'invalid value format error when saving details')
                },
                code=status.HTTP_400_BAD_REQUEST
            )

    @staticmethod
    def send_mail(request: request.Request):
        pass

    @staticmethod
    def verify_email(request: request.Request):
        pass