from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DirEnvio', '0002_alter_direccionenvio_default'), #Dependencia asignada
    ]

    operations = [
        migrations.AlterField(
            model_name='direccionenvio', #Le asignamos el name
            name='default', #Le asignamos el name
            field=models.BooleanField(default=False), #Este solo tendra 2 resultados o True or False
        ),
    ]
