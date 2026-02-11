from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer


@extend_schema_view(
    list=extend_schema(tags=["Categories"]),
    retrieve=extend_schema(tags=["Categories"]),
    create=extend_schema(tags=["Categories"]),
    update=extend_schema(tags=["Categories"]),
    partial_update=extend_schema(tags=["Categories"]),
    destroy=extend_schema(tags=["Categories"]),
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer
