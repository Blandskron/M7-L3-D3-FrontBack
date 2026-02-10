from django.contrib import admin
from ..models import BookCategory


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ("book", "category", "priority", "assigned_at")