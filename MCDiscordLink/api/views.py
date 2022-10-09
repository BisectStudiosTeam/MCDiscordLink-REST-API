from django.http.response import JsonResponse
from django.db.models.manager import BaseManager

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .serializers import PlayersSerializer
from .models import Players


def get_players(request) -> BaseManager[Players]:
    players = Players.objects.all()

    is_filtered = False
    code = None
    minecraft_name = None
    discord_id = None
    code = request.query_params.get("code", None)
    if code is not None:
        is_filtered = True
    else:
        minecraft_name = request.query_params.get("minecraft_name", None)
        if minecraft_name is not None:
            is_filtered = True
        else:
            discord_id = request.query_params.get("discord_id", None)
            if discord_id is not None:
                is_filtered = True
    if is_filtered:
        if code:
            players = players.filter(code=code)
        elif minecraft_name:
            players = players.filter(minecraft_name=minecraft_name)
        elif discord_id:
            players = players.filter(discord_id=discord_id)
    return players


@api_view(["GET", "POST", "DELETE"])
def players_list(request):
    if request.method == "GET":
        players = get_players(request)

        players_serializer = PlayersSerializer(players, many=True)
        return JsonResponse(players_serializer.data, safe=False)

    elif request.method == "POST":
        player_data = JSONParser().parse(request)
        players_serializer = PlayersSerializer(data=player_data)
        if players_serializer.is_valid():
            players_serializer.save()
            return JsonResponse(players_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(
            players_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        players = get_players(request)
        count = players.delete()
        return JsonResponse(
            {"message": f"{len(count)} Players' data was deleted!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "PUT", "DELETE"])
def players_detail(request, pk):
    try:
        player = Players.objects.get(pk=pk)
    except Players.DoesNotExist:
        return JsonResponse({"message": f"No player exists with pk {pk}"})

    if request.method == "GET":
        player_serializer = PlayersSerializer(player)
        return JsonResponse(player_serializer.data)

    elif request.method == "PUT":
        player_data = JSONParser().parse(request)
        player_serializer = PlayersSerializer(player, data=player_data)
        if player_serializer.is_valid():
            player_serializer.save()
            return JsonResponse(player_serializer.data)
        return JsonResponse(
            player_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        player.delete()
        return JsonResponse(
            {"message": "Player was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def players_linked(request):
    players = Players.objects.filter(discord_id=not None)

    if request.method == "GET":
        players_serializer = PlayersSerializer(players, many=True)
        return JsonResponse(players_serializer.data, safe=False)
