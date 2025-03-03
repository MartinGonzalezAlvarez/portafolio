# Generated by Django 5.1.5 on 2025-02-06 15:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('imagen', models.URLField()),
                ('precio', models.IntegerField()),
                ('estado', models.CharField(choices=[('disponible', 'Disponible'), ('arrendado', 'Arrendado'), ('mantencion', 'Mantención')], default='disponible', max_length=45)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='web.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Arriendo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('observacion', models.TextField(blank=True, null=True)),
                ('danado', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arriendos', to=settings.AUTH_USER_MODEL)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arriendos', to='web.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('cliente', 'Cliente'), ('operario', 'Operario')], default='cliente', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
