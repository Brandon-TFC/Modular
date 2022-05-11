
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DirEnvio', '0003_alter_direccionenvio_default'),
        ('orden', '0011_alter_orden_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='direccion_envio',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='DirEnvio.direccionenvio'),
            preserve_default=False,
        ),
    ]
