from urllib import response
from rest_framework import permissions
from django.contrib.auth.models import Group
from rest_framework.response import Response


class Custompermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role != 'student' and request.method in permissions.SAFE_METHODS:

            return True
        return False

    def has_object_permission(self, request, view, obj):
        '''safe method are get, hea'''
        if request.method in permissions.SAFE_METHODS and request.user.role != 'student':
            return True
        return False
