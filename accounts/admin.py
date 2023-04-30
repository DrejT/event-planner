from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserPost

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]
@admin.register(UserPost)
class UserPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":["title"]}


admin.site.register(CustomUser, CustomUserAdmin)
