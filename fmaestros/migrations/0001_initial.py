# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2021-02-16 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apunte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=60)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=12)),
                ('es_gasto', models.BooleanField()),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_paso_historico', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Apunte Contable',
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=16, unique=True)),
                ('nombre', models.CharField(max_length=60, unique=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_paso_historico', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Gastos e Ingresos',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=16, unique=True)),
                ('nombre', models.CharField(max_length=60, unique=True)),
                ('razon_social', models.CharField(blank=True, max_length=60, null=True)),
                ('cif', models.CharField(blank=True, max_length=16, null=True)),
                ('cp', models.CharField(blank=True, max_length=11, null=True)),
                ('direccion', models.CharField(blank=True, max_length=70, null=True)),
                ('poblacion', models.CharField(blank=True, max_length=70, null=True)),
                ('provincia', models.CharField(blank=True, max_length=70, null=True)),
                ('telefono', models.CharField(blank=True, max_length=70, null=True)),
                ('pais', models.CharField(blank=True, max_length=70, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_paso_historico', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=4, unique=True)),
                ('nombre', models.CharField(max_length=60)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_paso_historico', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Obras',
            },
        ),
        migrations.AddField(
            model_name='apunte',
            name='cuenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fmaestros.Cuenta'),
        ),
        migrations.AddField(
            model_name='apunte',
            name='obra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fmaestros.Obra'),
        ),
        migrations.AddIndex(
            model_name='apunte',
            index=models.Index(fields=['fecha'], name='fmaestros_a_fecha_0ca71c_idx'),
        ),
        migrations.AddIndex(
            model_name='apunte',
            index=models.Index(fields=['es_gasto'], name='fmaestros_a_es_gast_a2d771_idx'),
        ),
        migrations.AddIndex(
            model_name='apunte',
            index=models.Index(fields=['cuenta'], name='fmaestros_a_cuenta__010029_idx'),
        ),
        migrations.AddIndex(
            model_name='apunte',
            index=models.Index(fields=['obra'], name='fmaestros_a_obra_id_a461fd_idx'),
        ),
    ]
