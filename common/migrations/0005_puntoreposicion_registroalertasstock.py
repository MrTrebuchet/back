# Generated by Django 4.2 on 2023-10-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PuntoReposicion',
            fields=[
                ('idpuntoreposicion', models.AutoField(db_column='idPuntoReposicion', primary_key=True, serialize=False)),
                ('punto_reposicion', models.IntegerField(blank=True, null=True)),
                ('fecha_ultima_compra', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'punto_reposicion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegistroAlertasStock',
            fields=[
                ('idalerta', models.AutoField(db_column='idAlerta', primary_key=True, serialize=False)),
                ('descripcion_alerta', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_alerta', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'registro_alertas_stock',
                'managed': False,
            },
        ),
    ]
