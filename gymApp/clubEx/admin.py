from django.contrib import admin
from account.models import Account



class UserAdmin (admin.ModelAdmin):
    list_display = ('username','email','first_name', 'last_name', 'is_superuser', 'is_admin', 'is_staff', 'subscription_plan', 'phone_number')
    list_display_links = ('email', 'first_name', 'last_name')
    list_filter = ('first_name','last_name')
    search_fields = ('first_name', 'last_name', 'email')
    list_per_page = 25

admin.site.register(Account, UserAdmin)