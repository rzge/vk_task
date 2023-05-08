from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegisterForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)