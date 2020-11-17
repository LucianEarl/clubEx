from django.contrib import admin
from account.models import Account
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)
        
class UserAdmin (admin.ModelAdmin):
    list_display = ('username','email','first_name', 'last_name', 'is_superuser', 'is_admin', 'is_subscribed', 'subscription_plan', 'phone_number')
    list_display_links = ('email', 'first_name', 'last_name')
    list_filter = ('first_name','last_name')
    search_fields = ('first_name', 'last_name', 'email')
    list_per_page = 25

admin.site.register(Account, UserAdmin)
admin.site.register(Category, CategoryAdmin)