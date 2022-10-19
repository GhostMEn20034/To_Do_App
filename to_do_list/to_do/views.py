from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic.base import RedirectView
from django.views.generic import DetailView, UpdateView, DeleteView
import json
from .forms import TaskForm
from .models import Task, Category
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse, Http404
from .my_shortcuts import is_ajax, get_objects_or_none


# Create your views here.


class RedirectToBasePageView(RedirectView):
    pattern_name = 'redirect-to-base-page'

    def get_redirect_url(self, *args, **kwargs):
        return reverse("to_do:category")


def delete_category(request):
    if request.method == "POST":
        id_ = request.POST["cat_id"]
        category_obj = get_object_or_404(Category, id=id_)
        category_obj.delete()
        return HttpResponseRedirect(reverse("to_do:category"))


class CategoryView(View):
    template_name = "to_do/category.html"

    def get(self, request):
        categories = Category.objects.all()
        return render(request, self.template_name, {"categories": categories})

    def post(self, request):
        if "newCategory" in request.POST.keys():
            name = request.POST.get("newCategory")
            c = Category(name=name)
            c.save()
            return HttpResponseRedirect(reverse("to_do:category"))

        id_ = request.POST["id"]
        new_name = request.POST["new_name"]
        category_obj = get_object_or_404(Category, id=id_)
        category_obj.name = new_name
        category_obj.save()
        return HttpResponseRedirect(reverse("to_do:category"))


class Todos(View):
    template_name = "to_do/todo.html"
    form_class = TaskForm

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        uncompleted_tasks = get_objects_or_none(Task, category_id=category_id, execution_status=False)
        completed_tasks = get_objects_or_none(Task, category_id=category_id, execution_status=True)
        context = {
            "does_not_exist_msg": "There is no tasks yet",
            "category": category,
            "uncompleted_tasks": uncompleted_tasks,
            "completed_tasks": completed_tasks,
                }
        return render(request, self.template_name, context)

    def post(self, request, category_id):
        if is_ajax(request):
            if request.method == 'POST':
                data = json.load(request)
                todo = data.get('payload')
                task = get_object_or_404(Task, id=todo['id'])
                task.execution_status = not task.execution_status
                task.save()
                return JsonResponse({'status': 1,
                                     'done': task.execution_status})

        form = TaskForm(request.POST)
        category = Category.objects.get(id=category_id)
        if form.is_valid():
            form = form.save(commit=False)
            form.category = category
            form.save()
            return HttpResponseRedirect(reverse("to_do:to-do-list", kwargs={'category_id': category_id}))


class TaskDetailView(DetailView):
    model = Task
    template_name = "to_do/todo_detail.html"
    pk_url_kwarg = "task_id"

    def get_context_data(self, **kwargs):
        obj_id = Task.objects.get(id=self.kwargs['task_id']).category_id
        context = super().get_context_data(**kwargs)
        context["task_category"] = Category.objects.get(id=obj_id)
        return context


class TaskUpdateView(UpdateView):
    template_name = "to_do/update_todo.html"
    pk_url_kwarg = "task_id"
    form_class = TaskForm

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("task_id")
        return get_object_or_404(Task, id=id_)

    def get_success_url(self, **kwargs):
        obj_id = Task.objects.get(id=self.kwargs.get("task_id")).category_id
        return reverse("to_do:to-do-list", kwargs={'category_id': obj_id})


class TaskDeleteView(DeleteView):
    model = Task
    pk_url_kwarg = "task_id"

    def get_success_url(self, **kwargs):
        obj_id = Task.objects.get(id=self.kwargs.get("task_id")).category_id
        return reverse("to_do:to-do-list", kwargs={'category_id': obj_id})

    def get(self, request, *args, **kwargs):
        raise Http404
