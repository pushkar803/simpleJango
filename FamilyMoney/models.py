from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class FamilyMember(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='family_members')
    member = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='family_memberships')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.member.username}'
