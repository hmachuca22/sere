# Generated by Django 2.2.7 on 2019-12-15 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0022_auto_20191215_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='periodoext',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='sace',
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='identidadext',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.SACE'),
        ),
    ]
