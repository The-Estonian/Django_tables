from django.contrib import admin
from .models import Sales

# Register your models here.
@admin.register(Sales)
class PostsAdmin(admin.ModelAdmin):
    list_display = ["id", "Region", "Country"]