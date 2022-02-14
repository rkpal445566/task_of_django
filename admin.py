from django.contrib import admin
from app_1 .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'Email', 'password']
