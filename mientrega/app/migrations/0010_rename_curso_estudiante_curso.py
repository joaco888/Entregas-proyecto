# Generated by Django 4.2 on 2023-05-07 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_estudiante_email_alter_curso_jornada_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='curso',
            new_name='Curso',
        ),
    ]