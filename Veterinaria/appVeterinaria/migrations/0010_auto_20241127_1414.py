# Generated by Django 3.2 on 2024-11-27 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appVeterinaria', '0009_tbproducto_activo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbclientes',
            name='nid_cliente',
        ),
        migrations.RemoveField(
            model_name='tbclientes',
            name='nro_tel',
        ),
        migrations.AddField(
            model_name='tbclientes',
            name='nidCliente',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbclientes',
            name='nroTel',
            field=models.CharField(default='0000000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='cedula',
            field=models.ForeignKey(db_column='cedula', on_delete=django.db.models.deletion.CASCADE, to='appVeterinaria.persona'),
        ),
        migrations.AlterField(
            model_name='tbclientes',
            name='cedula',
            field=models.ForeignKey(blank=True, db_column='cedula', null=True, on_delete=django.db.models.deletion.SET_NULL, to='appVeterinaria.persona'),
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id_cita', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('motivo', models.TextField()),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appVeterinaria.persona')),
                ('mascota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appVeterinaria.mascota')),
            ],
            options={
                'db_table': 'cita',
            },
        ),
    ]
