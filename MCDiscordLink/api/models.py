from django.db import models

class Players(models.Model):
    code = models.CharField(max_length=5)
    minecraft_name = models.CharField(max_length=64)
    discord_id = models.CharField(max_length=20)
    
    def __str__(self):
        return f"<Player minecraft_name='{self.minecraft_name}' code='{self.code}' discord_id='{self.discord_id}'>"
    
    