from django.db import models
from .author import Author
from .category import Category


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
    )
    published_date = models.DateField(null=True, blank=True)
    categories = models.ManyToManyField(
        Category,
        through="BookCategory",
        related_name="books",
    )

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.title