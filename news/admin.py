from django.contrib import admin
from .models import News, Media, Url

class MediaInline(admin.TabularInline):
    model = Media
    extra = 0
    fields = ('media', 'media_type')

class UrlInline(admin.TabularInline):
    model = Url
    extra = 0
    fields = ('title', 'url')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    inlines = [MediaInline, UrlInline]
