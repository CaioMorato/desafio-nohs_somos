# Generated by Django 4.0.3 on 2022-03-28 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nohs_somos', '0005_alter_autores_id_autor_alter_autores_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autores',
            name='id_autor',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
