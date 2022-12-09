from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("activate/<uidb64>/<token>/", views.ActivateUserView.as_view(), name="activate-user"),
    path("registration_successful/", views.successful_registration, name="registration-successful"),
    path("confirm_email/", views.email_confirmation, name="email-confirmation"),
    path("password_reset/", views.ResetPasswordView.as_view(), name="password_reset"),
    path("password_reset_confirm/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html",
                                                     success_url=reverse_lazy("accounts:password_reset_complete")),
         name="password_reset_confirm"),
    path("password_reset_complete/",
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),
         name="password_reset_complete"),

]
