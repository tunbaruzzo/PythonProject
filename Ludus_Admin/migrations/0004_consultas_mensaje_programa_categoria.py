# Generated by Django 4.2.13 on 2024-06-11 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ludus_Admin', '0003_consultas_profesionales_profesion'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultas',
            name='mensaje',
            field=models.CharField(default='Sin Datos.', max_length=200),
        ),
        migrations.AddField(
            model_name='programa',
            name='categoria',
            field=models.CharField(choices=[('Cardio', 'Cardio'), ('Fuerza', 'Fuerza'), ('Movimiento', 'Movimiento'), ('Flexibilidad', 'Flexibilidad')], default='A definir manualmente.', max_length=40),
        ),
    ]
