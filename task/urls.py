from django.urls import path
from . import views

urlpatterns = [
    path(
        route='',
        view=views.TaskView.as_view(),
        name='role'
    ),
]