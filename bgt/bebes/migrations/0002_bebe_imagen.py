# Generated by Django 5.0.1 on 2024-01-14 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bebes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bebe',
            name='imagen',
            field=models.ImageField(default='default', upload_to='imagenes'),
            preserve_default=False,
        ),
    ]
