from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path(
        "",
        views.dashboard,
        name="dashboard"
    ),
    path(
        "register/",
        views.register,
        name="register"
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="files/login.html"
        ),
        name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),
    path(
        "upload/",
        views.upload_file,
        name="upload"
    ),
    path(
        "download/<int:file_id>/",
        views.download_file,
        name="download"
    ),
]