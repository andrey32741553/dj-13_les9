import csv
from .models import CSVPath, TableOption
from django.shortcuts import render


def table_view(request):
    CSV_FILENAME = (str(CSVPath.objects.last())).split("\\")[-1]
    CSV_FILENAME_PATH = str(CSVPath.objects.last())
    COLUMNS_from_DB = list(TableOption.objects.all())
    template = 'table.html'
    with open(CSV_FILENAME_PATH, 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            'columns': COLUMNS_from_DB,
            'table': table, 
            'csv_file': CSV_FILENAME
        }
        result = render(request, template, context)
    return result
