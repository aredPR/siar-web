from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    Descripción = models.TextField()

    def __str__(self):
        return f'Comment by { self.user.username}'
