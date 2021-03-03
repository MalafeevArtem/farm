from django.contrib import admin

from fields.models import Crop, Culture, Field, Season


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'square')
    list_filter = ('name', 'square')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('season',)
