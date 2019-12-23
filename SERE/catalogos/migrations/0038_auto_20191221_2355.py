# Generated by Django 2.1.1 on 2019-12-22 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0037_auto_20191221_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento', to='catalogos.Categoria', unique=True),
        ),
    ]