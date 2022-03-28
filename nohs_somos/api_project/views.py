from django.shortcuts import render
from rest_framework import viewsets
from nohs_somos.api_project.models import Autores, Livros
from nohs_somos.api_project.serializers import AutoresSerializer, LivrosSerializer

# Create your views here.


class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer


class AutoresViewSet(viewsets.ModelViewSet):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer
