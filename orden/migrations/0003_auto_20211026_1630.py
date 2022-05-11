
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orden', '0002_orden_ordenid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='envio_total',
        ),
        migrations.AlterField(
            model_name='orden',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
