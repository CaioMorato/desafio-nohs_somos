from django.db import models
from uuid import uuid4

# Create your models here.


class Livros(models.Model):
    id_livro = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)

    titulo = models.CharField(max_length=60)

    autor = models.CharField(max_length=50)

    ano_lancamento = models.IntegerField()

    preco = models.FloatField()

    data_criacao = models.DateField(auto_now_add=True)
