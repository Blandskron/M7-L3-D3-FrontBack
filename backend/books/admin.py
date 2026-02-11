from django.contrib import admin
from .models import Book, BookCategory


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "isbn")

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ("book", "category", "priority", "assigned_at")
