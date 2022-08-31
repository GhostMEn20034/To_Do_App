from django.shortcuts import render, redirect, reverse, get_object_or_404
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

    def get(self, request):
        categories = Category.objects.all()
        return render(request, self.template_name, {"categories": categories})

    def post(self, request):
        name = request.POST["name"]
        category = Category(name=name)
        category.save()
        return HttpResponseRedirect(reverse("to_do:category"))





class Todos(View):
    template_name = "to_do/todo.html"

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)  # get all Category objects
        try:
            todos = Task.objects.filter(category_id=category_id)# get all Task objects
        except (KeyError, Task.DoesNotExist):
            todos = None
        context = {
            "does_not_exist_msg": "There are no todos",
            "category": category,
            "todos": todos,
                }
        return render(request, self.template_name, context)
