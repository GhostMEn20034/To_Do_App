from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.views import View
from .forms import UserRegistrationForm


# Create your views here.
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
            account = authenticate(email=email, password=password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return HttpResponseRedirect(reverse('to_do:category'))
        else:
            context.update({'registration_form': form})
            print(form.errors)
    return render(request, template_name, context=context)
