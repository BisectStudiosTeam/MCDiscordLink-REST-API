from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import PlayersSerializer
from .models import Players


class PlayersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Players.objects.all().order_by("minecraft_name")
    serializer_class = PlayersSerializer
