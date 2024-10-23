from django.contrib import admin
from .models import (Vacation,
                     UserMessage,
                     TelegramUser,
                     Notification,
                     UserMessageFile,
                     UserMessageImage,
                     UserMessageVideo)

class NotificationInline(admin.TabularInline):
    model = Notification
    extra = 3
    fields = ['type', 'time']

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    inlines = [NotificationInline]


simple_models = [Vacation]
admin.site.register(simple_models)


class UserMessageImageInline(admin.TabularInline):
    model = UserMessageImage
    extra = 0
    fields = ('file_id',)

class UserMessageVideoInline(admin.TabularInline):
    model = UserMessageVideo
    extra = 0
    fields = ('file_id',)

class UserMessageFileInline(admin.TabularInline):
    model = UserMessageFile
    extra = 0
    fields = ('file_id',)

@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    inlines = (UserMessageImageInline, UserMessageVideoInline, UserMessageFileInline)

