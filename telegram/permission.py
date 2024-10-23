from django.conf import settings
from rest_framework import permissions


class HasValidTokenPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.headers.get('Authorization')
        security_token = settings.SECURITY_TOKEN

        return token == security_token
