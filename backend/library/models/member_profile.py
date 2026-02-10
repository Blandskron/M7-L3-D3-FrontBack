from django.db import models
from django.contrib.auth.models import User


class MemberProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="member_profile",
    )
    membership_id = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    joined_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "member_profile"

    def __str__(self):
        return f"{self.user.username} - {self.membership_id}"