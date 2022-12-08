from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("activate/<uidb64>/<token>/", views.ActivateUserView.as_view(), name="activate-user"),
    path("registration_successful/", views.successful_registration, name="registration-successful"),
    path("confirm_email/", views.email_confirmation, name="email-confirmation"),
]
