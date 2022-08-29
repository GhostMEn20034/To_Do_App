from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100) #Category name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Task(models.Model):
    task_title = models.CharField(max_length=255)
    task_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reminder_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, default="My day", on_delete=models.PROTECT)
    execution_status = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.task_title
