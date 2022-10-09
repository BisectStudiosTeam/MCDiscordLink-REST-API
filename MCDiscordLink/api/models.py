from django.db import models


class Players(models.Model):
    code = models.CharField(max_length=5, blank=False)
    minecraft_name = models.CharField(max_length=64, blank=False)
    discord_id = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"<Player minecraft_name='{self.minecraft_name}' code='{self.code}' discord_id='{self.discord_id}'>"
