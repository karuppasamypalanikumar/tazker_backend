from rest_framework import (
    request,
    status,
    serializers
)
from helpers import (
    validator
)

from . import (
    models as project_models,
    serializers as project_serializers
)

from django.utils.translation import gettext as _

class ProjectViewController():
    
    @staticmethod
    def get_projects(request: request.Request):
        user = request.user
        projects = project_models.Project.objects.filter(
            members__in=user
        )
        if projects:
            projects = project_serializers.ProjectSerializer(
                instance=projects,
                many=True
            )
            return projects

    @staticmethod
    def create_project(request: request.Request):
        pass

    @staticmethod
    def update_project(request: request.Request):
        pass

    @staticmethod
    def delete_projects(request: request.Request):
        pass