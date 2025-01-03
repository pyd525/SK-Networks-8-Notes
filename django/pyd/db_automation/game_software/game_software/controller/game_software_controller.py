import uuid

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

from game_software.serializer.game_software_list_serializer import GameSoftwareListSerializer
from game_software.service.game_software_service_impl import GameSoftwareServiceImpl
from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl


class GameSoftwareController(viewsets.ViewSet):
    gameSoftwareService = GameSoftwareServiceImpl.getInstance()
    redisCacheService = RedisCacheServiceImpl.getInstance()

    def requestGameSoftwareList(self, request):
        getRequest = request.GET
        page = int(getRequest.get("page", 1))
        perPage = int(getRequest.get("perPage", 12))
        paginatedGameSoftwareList, totalPages = self.gameSoftwareService.requestList(page, perPage)

        # serializer = GameSoftwareListSerializer(paginatedGameSoftwareList, many=True)

        return JsonResponse({"dataList": paginatedGameSoftwareList}, status=status.HTTP_200_OK)