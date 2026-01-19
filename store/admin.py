from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from .models import Product, Order

# -----------------------------
# REMOVE Groups from admin
# -----------------------------
admin.site.unregister(Group)


# -----------------------------
# Custom User Admin (no groups)
# -----------------------------
class CustomUserAdmin(UserAdmin):
    # ❌ Remove "Add user" permission
    def has_add_permission(self, request):
        return False
    
    # ❌ remove "By groups" filter
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    # ❌ remove groups field from user form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


# Re-register User model
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# -----------------------------
# Product Admin
# -----------------------------
admin.site.register(Product)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'payment_method', 'payment_status', 'created_at')

    def has_add_permission(self, request):
        return False

    
