from re import S
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True #Manejar errores

    dependencies = [ #Este es el ultimo archivo y ya no tendra dependencias mayores
    ]

    operations = [
        migrations.CreateModel( #Modelo creado
            name='Category', #Nombre a category
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), #Se le asigna lo que contendra
                ('title', models.CharField(max_length=40)), #Un titulo de maximo 40 caracteres
                ('description', models.TimeField()), #Description, tendra la hora asignada
                ('created_at', models.DateTimeField(auto_now_add=True)), #Una vez creado se le asignara la hora y la fecha en que fue creado
            ],
        ),
    ]
