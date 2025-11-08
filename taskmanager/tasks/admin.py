from django.contrib import admin
from tasks.models import Task, User

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'priority', 'completed')

# Register your models here.
admin.site.register(User)
admin.site.register(Task, TaskModelAdmin)