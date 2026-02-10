from django.urls import path
from . import views

urlpatterns = [
    path("", views.books_list, name="books_list"),
    path("authors/create/", views.author_create, name="author_create"),
    path("books/create/", views.book_create, name="book_create"),
]