from django.urls import path
from account import views

urlpatterns = [
    path(
        route='role/',
        view=views.RoleView.as_view(),
        name='role'
    ),
    path(
        route='signin/',
        view=views.SigninView.as_view(),
        name='signin'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='signout/',
        view=views.SignoutView.as_view(),
        name='signout'
    ), 
    path(
        route='profile/',
        view=views.ProfileView.as_view(),
        name='profile'
    ),
    path(
        route='verify-email/',
        view=views.EmailVerificationView.as_view(),
        name='verify-email'
    ),
]