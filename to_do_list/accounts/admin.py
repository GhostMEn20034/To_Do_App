from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_admin', 'last_login', 'is_active',)
    search_fields = ('username',)
    readonly_fields = ('id', 'date_joined', 'last_login',)
    filter_horizontal = ()
    ordering = ('id',)
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
