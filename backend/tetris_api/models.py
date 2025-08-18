from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    score = models.IntegerField()
    line_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games")

    def __str__(self):
        return str(self.score)