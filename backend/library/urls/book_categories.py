from rest_framework.routers import DefaultRouter
from ..views.book_category import BookCategoryViewSet

router = DefaultRouter()
router.register(
    r"",
    BookCategoryViewSet,
    basename="book-categories",
)

urlpatterns = router.urls