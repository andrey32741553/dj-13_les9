import glob
from django.db import models


COLUMNS = [
    {'name': 'id', 'width': 1},
    {'name': 'name', 'width': 3},
    {'name': 'price', 'width': 2},
    {'name': 'release_date', 'width': 2},
    {'name': 'lte_exists', 'width': 1},
]


class TableOption(models.Model):

    name = models.CharField("Название поля", max_length=60)
    width = models.PositiveIntegerField("Ширина поля", default=0)

    def __str__(self):
        return self.name


class CSVPath(models.Model):

    # def get_path(self):
    #
    #     root = '\\Users'
    #     name = 'phones_info.csv'
    #
    #     for self.csv_path in glob.iglob(f'{root}/**/{name}', recursive=True):
    #         self.save()
    #         return self.csv_path

    csv_path = models.CharField("Путь к CSV-файлу", blank=True, null=True, max_length=150)

    def __str__(self):
        return self.csv_path
