from django.contrib import admin
from .models import CustomUser, Task


admin.site.register(CustomUser)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    ordering = ('due_date',)

admin.site.register(Task, TaskAdmin)
