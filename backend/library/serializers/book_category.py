from rest_framework import serializers
from ..models import BookCategory


class BookCategorySerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source="book.title", read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = BookCategory
        fields = [
            "id",
            "book",
            "category",
            "book_title",
            "category_name",
            "priority",
            "assigned_at",
        ]