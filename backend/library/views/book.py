from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Book, Category, BookCategory
from ..serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author").prefetch_related("categories").order_by("id")
    serializer_class = BookSerializer

    @action(detail=True, methods=["post"])
    def add_category(self, request, pk=None):
        book = self.get_object()
        name = request.data.get("name")
        priority = request.data.get("priority", 1)

        if not name:
            return Response({"error": "name is required"}, status=400)

        category, _ = Category.objects.get_or_create(name=name)
        obj, created = BookCategory.objects.get_or_create(
            book=book,
            category=category,
            defaults={"priority": priority},
        )
        if not created:
            obj.priority = priority
            obj.save(update_fields=["priority"])

        return Response({"status": "ok"})