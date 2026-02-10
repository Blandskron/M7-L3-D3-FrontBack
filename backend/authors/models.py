from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "author"

    def __str__(self):
        return self.name