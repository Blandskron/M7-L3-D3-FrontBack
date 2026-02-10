from rest_framework import viewsets
from ..models import BookCategory
from ..serializers import BookCategorySerializer


class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.select_related("book", "category").order_by("id")
    serializer_class = BookCategorySerializer