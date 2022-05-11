
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orden', '0009_orden_promo_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='total',
            field=models.IntegerField(),
        ),
    ]
