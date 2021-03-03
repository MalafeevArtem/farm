from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Season(models.Model):
    name = models.CharField(max_length=4, unique=True)
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'


class Culture(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Культура'
        verbose_name_plural = 'Культуры'


class Field(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_fields')
    name = models.CharField("Название поля", max_length=64, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    square = models.PositiveIntegerField('Площадь поля')
    coordinate = models.CharField('Координаты поля', max_length=128)
    cadastral_number = models.CharField('Кадастровый номер', max_length=64)

    def __str__(self):
        return '{0} - {1}га'.format(self.name, self.square)

    class Meta:
        verbose_name = 'Поле'
        verbose_name_plural = 'Поля'

    def get_absolute_url(self):
        return reverse('fields:field_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        """Определяем автоматический slug, для несуществующих объектов."""
        if not self.id:
            self.slug = slugify(self.name)

        super(Field, self).save(*args, **kwargs)


class Crop(models.Model):
    season = models.ForeignKey(Season, related_name='crops', on_delete=models.CASCADE)
    field = models.ForeignKey(Field,  related_name='crops', on_delete=models.CASCADE)
    culture = models.ForeignKey(Culture, related_name='crops', on_delete=models.CASCADE)
    planned_harvest = models.IntegerField('Планируемый урожай', blank=True, null=True)
    actual_harvest = models.IntegerField('Фактический урожай', blank=True, null=True)
    sowing_date = models.DateField('Дата сева', blank=True, null=True)
    harvest_date = models.DateField('Дата сбора', blank=True, null=True)
    density = models.CharField('Плотность засева', max_length=32, blank=True, null=True)

    def __str__(self):
        return self.season.name

    class Meta:
        verbose_name = 'Сев'
        verbose_name_plural = 'Севы'
