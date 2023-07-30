"""
URL configuration for tazker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        route='admin/', 
        view=admin.site.urls,
        name="admin"
    ),
    path(
        route='',
        view=include('home.urls'),
        name='home'
    ),
    path(
        route='account/',
        view=include('account.urls'),
        name='account'
    ),
    path(
        route='notification/',
        view=include('notification.urls'),
        name='notification'
    ),
    path(
        route='task/',
        view=include('task.urls'),
        name='task'
    ),
    path(
        route='comment/',
        view=include('comment.urls'),
        name='comment'
    ),
    path(
        route='project/',
        view=include('project.urls'),
        name='project'
    ),
    path(
        route='chat/',
        view=include('chat.urls'),
        name='chat'
    ) 
]
