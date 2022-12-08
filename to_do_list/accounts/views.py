from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.utils.encoding import force_bytes, force_str
from django.views import View
from .forms import UserRegistrationForm, LoginUserForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .services.email_verification_token_generator import email_verification_token
from django.core.mail import EmailMessage
from .models import Account
# Create your views here.


def send_email_verification(user, request):
    current_site = get_current_site(request)
    subject = 'Confirm your email'
    body = render_to_string("accounts/email_confirmation.html", {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': email_verification_token.make_token(user),
    })

    msg = EmailMessage(subject=subject, body=body, to=[user.email])
    msg.content_subtype = "html"
    msg.send()


def register_user(request, *args, **kwargs):
    template_name = "accounts/register.html"
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You're already authenticated as {user.email}")
    context = {}

    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            password = form.cleaned_data.get('password1')
            user = Account.objects.get(email=email)
            request.session.update({"email": email})
            send_email_verification(user, request)
            return HttpResponseRedirect(
                reverse('accounts:email-confirmation'))
        else:
            context.update({'registration_form': form})
            print(form.errors)
    return render(request, template_name, context=context)


def successful_registration(request):
    return render(request, "accounts/registration_successful.html")


def email_confirmation(request):
    return render(request, "accounts/confirm_email.html", {'email': request.session.get("email")})


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = "accounts/login.html"


def logout_view(request):
    logout(request)
    return redirect("accounts:login")


class ActivateUserView(View):
    def get_user_from_email_verification_token(self, uidb64, token: str):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = Account.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
            return None

        if user is not None and email_verification_token.check_token(user, token):
            return user

        return None

    def get(self, request, uidb64, token):
        user = self.get_user_from_email_verification_token(uidb64, token)
        user.is_active = True
        user.save()
        login(request, user, backend='accounts.backends.CaseInsensitiveModelBackend')
        return redirect("accounts:registration-successful")
