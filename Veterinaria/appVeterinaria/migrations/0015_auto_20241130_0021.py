# Generated by Django 3.2 on 2024-11-30 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appVeterinaria', '0014_auto_20241129_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagos',
            name='id_fact',
            field=models.ForeignKey(blank=True, db_column='idFact', null=True, on_delete=django.db.models.deletion.SET_NULL, to='appVeterinaria.tbencabfacvta'),
        ),
        migrations.AlterField(
            model_name='tbdetfactvta',
            name='idFact',
            field=models.ForeignKey(db_column='idFact', on_delete=django.db.models.deletion.CASCADE, to='appVeterinaria.tbencabfacvta'),
        ),
        migrations.AlterField(
            model_name='tbdetfactvta',
            name='idProducto',
            field=models.ForeignKey(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, to='appVeterinaria.tbproducto'),
        ),
        migrations.AlterField(
            model_name='tbdetfactvta',
            name='valVenta',
            field=models.FloatField(db_column='valVenta'),
        ),
        migrations.AlterField(
            model_name='tbencabfacvta',
            name='nidCliente',
            field=models.ForeignKey(db_column='nidCliente', on_delete=django.db.models.deletion.CASCADE, to='appVeterinaria.tbclientes'),
        ),
    ]
