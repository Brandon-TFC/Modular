from django.db import migrations, models


class Migration(migrations.Migration): #Vamos a migrar lo de este archivo a otro

    dependencies = [
        ('categories', '0001_initial'), #Se le asigna el initial ya que es al archivo que ira ligado
    ]

    operations = [
        migrations.AlterField(
            model_name='category', #Le asignamos nombre
            name='description',  #Le asignamos nombre
            field=models.TextField(), #Le asignamos escritura
        ),
    ]
