# Generated by Django 2.2.7 on 2019-12-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0008_remove_categoria_cod_depto'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='codigop',
            field=models.IntegerField(default=0),
        ),
    ]
