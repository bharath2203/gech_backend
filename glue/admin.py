from django.contrib import admin
from .models import Notification, CoreMember, GlueBlog

admin.site.register(Notification)
admin.site.register(CoreMember)
admin.site.register(GlueBlog)