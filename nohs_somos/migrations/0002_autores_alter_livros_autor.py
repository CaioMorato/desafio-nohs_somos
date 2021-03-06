# Generated by Django 4.0.3 on 2022-03-28 04:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('nohs_somos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id_autor', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='livros',
            name='autor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='nohs_somos.autores'),
        ),
    ]
