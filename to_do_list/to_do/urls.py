from django.urls import path
from . import views

app_name = "to_do"
urlpatterns = [
    path('', views.RedirectToBasePageView.as_view(), name='redirect-to-base-page'),
    path('tasks/categories/', views.CategoryView.as_view(), name="category"),
    path('tasks/category/<int:category_id>/', views.Todos.as_view(), name="to-do-list"),
    path('tasks/detail/<int:task_id>/', views.TaskDetailView.as_view(), name="to-do-detail"),
    path('tasks/edit/<int:task_id>/', views.TaskUpdateView.as_view(), name="to-do-edit"),
    path('tasks/delete/<int:task_id>/', views.TaskDeleteView.as_view(), name="to-do-delete"),
    path('tasks/categories/delete/', views.delete_category, name="category-delete"),
    path('tasks/task_search', views.TaskSearch.as_view(), name="task-search"),
]
