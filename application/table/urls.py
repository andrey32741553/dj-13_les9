from django.urls import path
from table.views import table_view

urlpatterns = [
    path('table/', table_view)
]
