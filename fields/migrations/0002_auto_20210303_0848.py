# Generated by Django 3.1.7 on 2021-03-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crop',
            options={'verbose_name': 'Сев', 'verbose_name_plural': 'Севы'},
        ),
        migrations.AlterModelOptions(
            name='culture',
            options={'verbose_name': 'Культура', 'verbose_name_plural': 'Культуры'},
        ),
        migrations.AlterModelOptions(
            name='field',
            options={'verbose_name': 'Поле', 'verbose_name_plural': 'Поля'},
        ),
        migrations.AlterModelOptions(
            name='season',
            options={'verbose_name': 'Сезон', 'verbose_name_plural': 'Сезоны'},
        ),
        migrations.AlterField(
            model_name='crop',
            name='actual_harvest',
            field=models.IntegerField(blank=True, verbose_name='Фактический урожай'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='harvest_date',
            field=models.DateField(blank=True, verbose_name='Дата сбора'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='planned_harvest',
            field=models.IntegerField(blank=True, verbose_name='Планируемый урожай'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='sowing_date',
            field=models.DateField(blank=True, verbose_name='Дата сева'),
        ),
    ]
