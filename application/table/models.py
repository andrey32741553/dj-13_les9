import glob
from django.db import models


class TableOption(models.Model):

    name = models.CharField("Название поля", max_length=60)
    width = models.PositiveIntegerField("Ширина поля", default=0)

    def __str__(self):
        return self.name


class CSVPath(models.Model):

    def get_path(self):

        root = '\\Users'
        name = 'phones_info.csv'

        for self.csv_path in glob.iglob(f'{root}/**/{name}', recursive=True):
            self.save()
            return self.csv_path

    def __str__(self):
        return self.csv_path

    csv_path = models.FilePathField("Путь к CSV-файлу", blank=True, null=True)
