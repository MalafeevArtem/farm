# Generated by Django 3.1.7 on 2021-03-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0004_auto_20210303_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Название поля'),
        ),
    ]
