# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2021-02-11 15:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IPPermitida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('descripcion', models.CharField(blank=True, default=None, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'IPs Permitidas para Login',
            },
        ),
        migrations.CreateModel(
            name='LogAcceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
                ('username', models.CharField(max_length=30)),
                ('ip', models.GenericIPAddressField()),
                ('correcto', models.BooleanField(default=False)),
                ('comentario', models.CharField(blank=True, default=None, max_length=32, null=True)),
            ],
            options={
                'verbose_name_plural': 'Logs de Acceso por Login',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('nombre', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('apellidos', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('email', models.CharField(blank=True, default=None, max_length=75, null=True)),
                ('esta_activo', models.BooleanField(default=True)),
                ('ultimo_acceso_correcto', models.DateTimeField(blank=True, default=None, null=True)),
                ('nif', models.CharField(blank=True, default=None, max_length=15, null=True, unique=True)),
                ('observaciones', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('ultimo_acceso_incorrecto', models.DateTimeField(blank=True, default=None, null=True)),
                ('accesos_correctos', models.PositiveSmallIntegerField(default=0)),
                ('accesos_incorrectos', models.PositiveSmallIntegerField(default=0)),
                ('fecha_baja', models.DateField(blank=True, null=True)),
                ('es_admin', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_paso_historico', models.DateTimeField(blank=True, default=None, null=True)),
                ('dj_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.AddIndex(
            model_name='usuario',
            index=models.Index(fields=[b'username'], name='usuarios_us_usernam_a1b21e_idx'),
        ),
        migrations.AddIndex(
            model_name='usuario',
            index=models.Index(fields=[b'es_admin'], name='usuarios_us_es_admi_6a9927_idx'),
        ),
        migrations.AddIndex(
            model_name='usuario',
            index=models.Index(fields=[b'fecha_paso_historico'], name='usuarios_us_fecha_p_5bc436_idx'),
        ),
    ]
