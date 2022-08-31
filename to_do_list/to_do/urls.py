from django.urls import path
from . import views

app_name = "to_do"
urlpatterns = [
    path('', views.RedirectToBasePageView.as_view(), name='redirect-to-base-page'),
    path('category/', views.CategoryView.as_view(), name="category"),
    path('category/<int:category_id>/', views.Todos.as_view(), name="to-do-list"),
]
