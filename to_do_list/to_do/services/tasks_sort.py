from django.db.models import F


class TaskSort:
    def __init__(self, queryset):
        self.queryset = queryset

    def sort_by_reminder_date(self):
        return self.queryset.order_by(F('reminder_date').asc(nulls_last=True))

    def sort_by_creation_date(self):
        return self.queryset.order_by('created_at')

    def sort_alphabetically(self):
        return self.queryset.order_by('task_title')

    def sort(self, request):
        query = request.GET

        match query.get('sort_condition'):
            case 'reminder_date':
                return self.sort_by_reminder_date()
            case 'creation_date':
                return self.sort_by_creation_date()
            case 'alphabetically':
                return self.sort_alphabetically()
