from django.contrib import admin

from .models import CheckList

models = (CheckList, )
admin.site.register(models)
