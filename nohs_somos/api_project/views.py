from django.shortcuts import render
from rest_framework import viewsets
from nohs_somos.api_project.models import Livros
from nohs_somos.api_project.serializers import LivrosSerializer

# Create your views here.


class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
