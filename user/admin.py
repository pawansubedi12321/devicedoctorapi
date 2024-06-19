from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import AddCategory,Problem,Question,Answer,createBooking,User
from django.contrib.auth.models import   Permission
class createBookingInline(admin.TabularInline):
    model = createBooking
    extra = 1  # Number of extra forms to show

class createprobleminline(admin.ModelAdmin):
    inlines = [createBookingInline]
      


class CustomUserAdmin(UserAdmin):
    # Specify the fieldsets
    fieldsets = (
        # (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('username','phone_number','password','gender', 'district', 'profile_image', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser','is_admin','is_customer','groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Register User model with CustomUserAdmin
admin.site.register(User, CustomUserAdmin)

# Register Permission model
from django.contrib.auth.models import Permission
admin.site.register(Permission)
admin.site.register(AddCategory)
admin.site.register(Problem,createprobleminline)
admin.site.register(Question)
admin.site.register(Answer)

