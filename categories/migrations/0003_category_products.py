from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [ #Hacemos dependencias
        ('products', '0002_auto_20211018_1536'), #Se le asigna este valor ya que fue el arrojado por el admin
        ('categories', '0002_alter_category_description'), #Para poder unir con otro archivo
    ]

    operations = [
        migrations.AddField(
            model_name='category', #Le asignamos nombre
            name='products', #Le asignamos nombre
            field=models.ManyToManyField(to='products.Product'), #Especificamos la relacion que tendran los productos
        ),
    ]
