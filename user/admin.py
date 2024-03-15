from django.contrib import admin

# Register your models here.
from .models import AddCategory,Problem,Question,Answer,createBooking,Register
# Register your models here.


admin.site.register(AddCategory)
admin.site.register(Problem)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(createBooking)
admin.site.register(Register)