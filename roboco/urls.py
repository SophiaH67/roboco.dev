"""roboco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from roboco import views
from invites import views as invite_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("why", views.why, name="why"),
    # User views
    path("", include("users.urls")),
    # Invite views
    path("invite/", invite_views.invite_user, name="invite_user"),
    # Nginx
    path("nginx/", include("nginx.urls")),
    # Django Reload
    path("__reload__/", include("django_browser_reload.urls")),
]
