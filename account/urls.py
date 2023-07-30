from django.urls import path
from account import views

urlpatterns = [
    path(
        route='role/',
        view=views.RoleView.as_view(),
        name='role'
    )
]