from django.db import models
from .book import Book
from .category import Category


class BookCategory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    assigned_at = models.DateField(auto_now_add=True)
    priority = models.PositiveSmallIntegerField(default=1)

    class Meta:
        db_table = "book_category"
        unique_together = ("book", "category")

    def __str__(self):
        return f"{self.book.title} - {self.category.name}"