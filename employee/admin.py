from django.contrib import admin
from .models import Employee
from .models import BlogPosts
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(BlogPosts)