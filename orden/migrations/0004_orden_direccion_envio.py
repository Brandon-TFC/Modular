
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DirEnvio', '0001_initial'),
        ('orden', '0003_auto_20211026_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='direccion_envio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DirEnvio.direccionenvio'),
        ),
    ]
