from django.contrib import admin
from .models import Student, Student_name
# Register your models here.

@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
	list_display=('id','name','roll','city')

@admin.register(Student_name)
class Student_name_admin(admin.ModelAdmin):
	list_display=('id','name')