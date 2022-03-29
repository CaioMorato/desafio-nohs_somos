from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from nohs_somos.api_project.models import Autores
from nohs_somos.api_project.serializers import AutoresSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def listar_salvar_autores(request):
    if request.method == 'GET':
        autores = Autores.objects.all()
        serializer = AutoresSerializer(autores, many=True)

        if len(serializer.data) < 1:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AutoresSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deletar_autores(request, pk):
    try:
        autor = Autores.objects.get(pk=pk)
    except Autores.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
