from django.urls import path
from .views import List_data_view, Add_expenditure_view, clear_expenditure_table

app_name = 'dca'

urlpatterns = [
    path('', List_data_view.as_view(), name='datacollector-home'),
    path('add_expenditure/', Add_expenditure_view.as_view(), name='data-exp-add'),
    path('clear_table/', clear_expenditure_table, name="clear-expenditure"),
]
