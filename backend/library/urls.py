from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, CategoryViewSet, BookCategoryViewSet

router = DefaultRouter()
router.register(r"authors", AuthorViewSet, basename="authors")
router.register(r"books", BookViewSet, basename="books")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"book-categories", BookCategoryViewSet, basename="book-categories")

urlpatterns = [
    path("", include(router.urls)),
]