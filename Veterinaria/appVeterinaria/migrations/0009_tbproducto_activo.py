# Generated by Django 3.2 on 2024-11-26 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appVeterinaria', '0008_auto_20241123_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbproducto',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
