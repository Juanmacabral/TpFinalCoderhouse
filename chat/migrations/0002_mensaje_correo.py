# Generated by Django 4.1.5 on 2023-01-22 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='correo',
            field=models.EmailField(default='sin correo', max_length=255),
        ),
    ]
