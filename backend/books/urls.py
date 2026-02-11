from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookCategoryViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet, basename="books")
router.register(r"book-categories", BookCategoryViewSet, basename="book-categories")

urlpatterns = router.urls