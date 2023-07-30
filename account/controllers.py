from rest_framework import (
    request,
    response,
    serializers,
    status
)
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
        name = validator.check_role_name(request=request)
        project = validator.check_role_project_status(request=request)
        task = validator.check_role_task_status(request=request)
        comment = validator.check_role_comment_status(request=request)
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
        id = validator.check_role_id(request=request)
        name = request.data.get("name")
        task = request.data.get("task")
        comment = request.data.get("comment")
        project = request.data.get("project")
        try:
            role = account_models.Role.objects.get(id=id)
            if name:
                name = validator.check_role_name(request=request)
                role.name = name
            if task:
                task = validator.check_role_task_status(request=request)
                role.task = task
            if comment:
                comment = validator.check_role_comment_status(request=request)
                role.comment = comment
            if project:
                project = validator.check_role_project_status(request=request)
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
        id = validator.check_role_id(request=request)
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