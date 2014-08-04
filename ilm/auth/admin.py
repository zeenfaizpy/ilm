from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms

from .models import UserProfile

admin.site.register(UserProfile)