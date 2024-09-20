# Generated by Django 5.1.1 on 2024-09-20 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id_reporte', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Analisis',
            fields=[
                ('id_analisis', models.AutoField(primary_key=True, serialize=False)),
                ('kpi_nombre', models.CharField(max_length=45)),
                ('kpi_valor', models.IntegerField()),
                ('fecha', models.DateField()),
                ('reporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.reporte')),
            ],
        ),
    ]