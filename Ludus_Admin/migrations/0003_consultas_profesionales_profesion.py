# Generated by Django 4.2.13 on 2024-06-04 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ludus_Admin', '0002_instructores_miembros_profesionales'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='profesionales',
            name='profesion',
            field=models.CharField(default='Indefinida', max_length=40),
        ),
    ]
