# Generated by Django 4.2 on 2023-05-01 01:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_entregable_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregable',
            name='fecha_entrega',
            field=models.DateField(default=datetime.date.today),
        ),
    ]