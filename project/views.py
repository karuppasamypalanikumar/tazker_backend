from rest_framework import (
    response,
    request,
    views,
    status
)
from . import (
    controllers as project_controllers
)
from django.utils.translation import gettext as _

# Create your views here.
class ProjectView(views.APIView):
    def get(self, request: request.Request):
        projects = project_controllers.ProjectViewController.get_projects(request=request)
        return response.Response(
            data={
                'status_code' : _('1'),
                'status_message' : _('Data fetched successfully'),
                'data' : projects
            },
            status=status.HTTP_200_OK
        )
    def post(self, request: request.Request):
        project = project_controllers.ProjectViewController.create_project(request=request)
        return response.Response(
            data={
                'status_code' : _('1'),
                'status_message' : _('Project created successfully'),
                'data' : project
            },
            status=status.HTTP_200_OK
        )
    def put(self, request: request.Request):
        project = project_controllers.ProjectViewController.update_project(request=request)
        return response.Response(
            data={
                'status_code' : _('1'),
                'status_message' : _('Project updated successfully'),
                'data' : project
            },
            status=status.HTTP_200_OK
        )
    def delete(self, request: request.Request):
        project_controllers.ProjectViewController.delete_projects(request=request)
        return response.Response(
            data={
                'status_code' : _('1'),
                'status_message' : _('Project deleted successfully'),
            },
            status=status.HTTP_200_OK
        )