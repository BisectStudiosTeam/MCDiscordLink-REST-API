from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Players


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ("id", "code", "minecraft_name", "discord_id")
