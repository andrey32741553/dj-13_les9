from django.contrib import admin
from django.contrib.admin import ModelAdmin

from table.models import TableOption, CSVPath


@admin.register(TableOption)
class TableOptionAdmin(ModelAdmin):
    """Категории"""
    list_display = ("id", "name", "width")


@admin.register(CSVPath)
class CSVPathAdmin(ModelAdmin):
    """Категории"""
    list_display = ("csv_path",)
