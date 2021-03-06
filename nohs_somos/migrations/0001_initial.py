# Generated by Django 4.0.3 on 2022-03-28 03:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id_livro', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=60)),
                ('autor', models.CharField(max_length=50)),
                ('ano_lancamento', models.IntegerField()),
                ('preco', models.FloatField()),
                ('data_criacao', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
