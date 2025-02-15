# Generated by Django 3.2 on 2024-11-20 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appVeterinaria', '0005_auto_20241116_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='banners',
        ),
        migrations.AddField(
            model_name='configuracionempresa',
            name='banner',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='configuracionempresa',
            name='banner1',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='configuracionempresa',
            name='banner2',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='configuracionempresa',
            name='banner3',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='configuracionempresa',
            name='banner4',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='configuracionempresa',
            name='banner5',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='configuracionempresa',
            name='banner6',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tbproducto',
            name='id_categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appVeterinaria.tbcategorias'),
        ),
    ]
