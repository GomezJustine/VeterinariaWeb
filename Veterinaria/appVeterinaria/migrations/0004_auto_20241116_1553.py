# Generated by Django 3.2 on 2024-11-16 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appVeterinaria', '0003_banners'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Banners',
        ),
        migrations.RenameField(
            model_name='configuracionempresa',
            old_name='banner',
            new_name='banners',
        ),
    ]
