from django.contrib import admin
from .models import Student, Notification, Department, Faculty

admin.site.register(Student)
admin.site.register(Notification)
admin.site.register(Department)
admin.site.register(Faculty)