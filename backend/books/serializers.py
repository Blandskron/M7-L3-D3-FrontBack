from rest_framework import serializers
from .models import Book, BookCategory
from categories.models import Category
from authors.views import  Author
from authors.serializers import AuthorSerializer
from categories.serializers import CategorySerializer


class BookCategoryWriteSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    priority = serializers.IntegerField(min_value=1, required=False, default=1)


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source="author",
        queryset=Author.objects.all(),
        write_only=True,
    )
    categories = CategorySerializer(many=True, read_only=True)
    categories_input = BookCategoryWriteSerializer(
        many=True,
        write_only=True,
        required=False,
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "isbn",
            "published_date",
            "author",
            "author_id",
            "categories",
            "categories_input",
        ]

    def create(self, validated_data):
        categories_payload = validated_data.pop("categories_input", [])
        book = Book.objects.create(**validated_data)

        for item in categories_payload:
            category, _ = Category.objects.get_or_create(name=item["name"])
            BookCategory.objects.create(
                book=book,
                category=category,
                priority=item.get("priority", 1),
            )

        return book
    

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