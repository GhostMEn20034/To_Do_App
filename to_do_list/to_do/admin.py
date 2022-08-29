from django.contrib import admin
from .models import Category, Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_title', 'task_text', 'created_at', 'reminder_date', 'category', 'execution_status')
    list_display_links = ('id', 'task_title')
    search_fields = ('id', 'task_title')
    list_editable = ('execution_status', )
    list_filter = ('execution_status', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
