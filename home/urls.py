from django.urls import path
from home import views

urlpatterns = [
    path(
        route='',
        view=views.HomeView.as_view(),
        name="home_index"
    ),
    path(
        route='health_check/',
        view=views.HealthCheckView.as_view(),
        name="home_health_check"
    )
]