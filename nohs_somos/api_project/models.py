from django.db import models

# Create your models here.


class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=60, unique=True)

    nascimento = models.IntegerField()

    def __str__(self) -> str:
        return self.nome


class Livros(models.Model):
    id_livro = models.AutoField(primary_key=True)

    titulo = models.CharField(max_length=60)

    autor = models.ForeignKey(
        Autores,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        to_field='id_autor'
    )

    ano_lancamento = models.IntegerField()

    preco = models.FloatField()

    data_criacao = models.DateField(auto_now_add=True)
