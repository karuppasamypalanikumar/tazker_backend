from rest_framework import (
    request,
    serializers,
    status
)
from django.utils.translation import gettext as _

def check_role_name(request: request.Request):
    data = request.data
    name = data.get('name')
    if not name:
        raise serializers.ValidationError(
            detail={
                'status_code': _('0'),
                'status_message': _('role name field is required')
            },
            code=status.HTTP_400_BAD_REQUEST
        )
    try:
        name = str(name)
    except ValueError:
        raise serializers.ValidationError(
            detail={
                'status_code': _('0'),
                'status_message': _('role name invalid format')
            },
            code=status.HTTP_400_BAD_REQUEST
        )
    if len(name) > 100:
        raise serializers.ValidationError(
            detail={
                'status_code': _('0'),
                'status_message': _('role name max len 100 char')
            },
            code=status.HTTP_400_BAD_REQUEST
        )
    return name

def check_role_task_status(request: request.Request):
    data = request.data
    task = data.get('task')
    if not task:
        raise serializers.ValidationError(
            detail={
                'status_code': _('0'),
                'status_message': _('role task field is required')
            },
            code=status.HTTP_400_BAD_REQUEST
        )
    try:
        task = eval(task.title())
    except ValueError:
        raise serializers.ValidationError(
            detail={
                'status_code': _('0'),
                'status_message': _('role task invalid format')
            },
            code=status.HTTP_400_BAD_REQUEST
        )
    return task

def check_role_id(request: request.Request):
    data = request.data
    id = data.get('id')
    if not id:
        raise serializers.ValidationError(
            detail={
                'status_code': _('0'),
                'status_message': _('role id field is required')
            },
            code=status.HTTP_400_BAD_REQUEST
        )
    try:
        id = int(id)
    except ValueError:
        raise serializers.ValidationError(
            detail={
                'status_code': _('0'),
                'status_message': _('role id invalid format')
            },
            code=status.HTTP_400_BAD_REQUEST
        )
    return id

def check_role_comment_status(request: request.Request):
    data = request.data
    comment = data.get('comment')
    if not comment:
        raise serializers.ValidationError(
            detail={
                'status_code': _('0'),
                'status_message': _('role comment field is required')
            },
            code=status.HTTP_400_BAD_REQUEST
        )
    try:
        comment = eval(comment.title())
    except ValueError:
        raise serializers.ValidationError(
            detail={
                'status_code': _('0'),
                'status_message': _('role comment invalid format')
            },
            code=status.HTTP_400_BAD_REQUEST
        )
    return comment

def check_role_project_status(request: request.Request):
    data = request.data
    project = data.get('project')
    if not project:
        raise serializers.ValidationError(
            detail={
                'status_code': _('0'),
                'status_message': _('role project field is required')
            },
            code=status.HTTP_400_BAD_REQUEST
        )
    try:
        project = eval(project.title())
    except ValueError:
        raise serializers.ValidationError(
            detail={
                'status_code': _('0'),
                'status_message': _('role project invalid format')
            },
            code=status.HTTP_400_BAD_REQUEST
        )
    return project