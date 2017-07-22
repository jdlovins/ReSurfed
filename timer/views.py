from django.shortcuts import render
from rest_framework import generics
from .models import Map, Server, Player, Time
from .serializers import MapSerializer, ServerSerializer, PlayerSerializer, TimeSerializer
from .filters import MapFilter, TimeFilter


class MapList(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    filter_class = MapFilter


class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class ServerList(generics.ListCreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TimeList(generics.ListCreateAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    filter_class = TimeFilter


class TimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
