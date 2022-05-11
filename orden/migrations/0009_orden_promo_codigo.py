
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promo_codigo', '0001_initial'),
        ('orden', '0008_alter_orden_direccion_envio'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='promo_codigo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promo_codigo.promocodigo'),
        ),
    ]
