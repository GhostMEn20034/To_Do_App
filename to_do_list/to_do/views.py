from django.shortcuts import render, redirect, reverse
from django.views.generic.base import RedirectView
from .models import Task, Category
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.

class RedirectToBasePageView(RedirectView):
    pattern_name = 'redirect-to-base-page'

    def get_redirect_url(self, *args, **kwargs):
        return 'category/'


class CategoryView(View):
    template_name = "to_do/category.html"

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, self.template_name, {"categories": categories})

    def post(self, request, *args, **kwargs):
        name = request.POST["name"]
        category = Category(name=name)
        category.save()
        return HttpResponseRedirect(reverse("to_do:category"))




def todo(request):
    todos = Task.objects.all()  # get all Task objects
    categories = Category.objects.all()  # get all Category objects
    return render(request, "to_do/todo.html", {"todos": todos, "categories": categories})