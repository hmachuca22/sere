# Generated by Django 2.2.7 on 2019-12-16 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0030_productointerno_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productointerno',
            name='sexo',
        ),
    ]
