from django.db import models

class PlayerStat(models.Model):
    player_id = models.IntegerField(unique=True)
    nickname = models.CharField(max_length=100)
    profile_image = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.nickname} - {self.score}"

