# Generated by Django 2.2.7 on 2019-12-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0021_auto_20191215_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sace',
            name='id',
        ),
        migrations.AlterField(
            model_name='sace',
            name='identidadsace',
            field=models.CharField(max_length=13, primary_key=True, serialize=False),
        ),
    ]
