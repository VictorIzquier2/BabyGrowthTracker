# Generated by Django 5.0.1 on 2024-01-11 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bebes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('especialista', models.CharField(max_length=250)),
                ('cita', models.JSONField(default=dict)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('confirmada', 'Confirmada'), ('cancelada', 'Cancelada')], max_length=10)),
                ('mensaje', models.TextField()),
                ('bebe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bebes.bebe')),
            ],
        ),
    ]
