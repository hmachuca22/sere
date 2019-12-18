# Generated by Django 2.2.7 on 2019-12-12 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salidas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SACEdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('idalumno', models.DateField()),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('grado', models.CharField(blank=True, max_length=2, null=True)),
                ('nivel', models.CharField(blank=True, max_length=50, null=True)),
                ('codce', models.CharField(blank=True, max_length=50, null=True)),
                ('nombrece', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('observacion', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Datos SACE',
                'verbose_name_plural': 'Datos SACE',
            },
        ),
    ]
