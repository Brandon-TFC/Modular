from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DirEnvio', '0001_initial'), #Dependencia asignada
    ]

    operations = [
        migrations.AlterField(
            model_name='direccionenvio', #Le asignamos un nombre
            name='default', #Le asignamos un default en caso de tener nada
            field=models.BooleanField(default=True), #Solo tendra 2 resultados o True or False
        ),
    ]
