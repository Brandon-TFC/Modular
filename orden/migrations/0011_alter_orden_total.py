
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orden', '0010_alter_orden_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
