# Generated by Django 4.1.5 on 2023-12-13 02:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0004_alter_actividadmodel_fecha_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadmodel',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 13, 2, 47, 38, 523485, tzinfo=datetime.timezone.utc)),
        ),
    ]
