# Generated by Django 2.1.1 on 2020-01-04 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0043_auto_20200103_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productointerno',
            name='estado',
            field=models.IntegerField(max_length=2),
        ),
    ]
