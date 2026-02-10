from django.urls import path, include

urlpatterns = [
    path("authors/", include("library.urls.authors")),
    path("books/", include("library.urls.books")),
    path("categories/", include("library.urls.categories")),
    path("book-categories/", include("library.urls.book_categories")),
]
