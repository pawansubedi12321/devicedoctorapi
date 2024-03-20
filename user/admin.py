from django.contrib import admin

# Register your models here.
from .models import AddCategory,Problem,Question,Answer,createBooking,Register

class createBookingInline(admin.TabularInline):
    model = createBooking
    extra = 1  # Number of extra forms to show

class createprobleminline(admin.ModelAdmin):
    inlines = [createBookingInline]
       
admin.site.register(AddCategory)
# admin.site.register(Problem)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Problem,createprobleminline)
admin.site.register(Register)