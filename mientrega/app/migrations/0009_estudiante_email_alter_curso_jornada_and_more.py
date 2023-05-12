# Generated by Django 4.2 on 2023-05-07 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_profesor_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curso',
            name='Jornada',
            field=models.CharField(choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino')], max_length=100),
        ),
        migrations.AlterField(
            model_name='curso',
            name='Tipo',
            field=models.CharField(choices=[('Carrera', 'Carrera'), ('Curso', 'Curso')], max_length=100),
        ),
    ]