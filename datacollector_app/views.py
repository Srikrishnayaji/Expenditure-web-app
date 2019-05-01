from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView
from .models import Expenditure_data
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# creating home view
class List_data_view(LoginRequiredMixin, ListView):  # list.html
    model = Expenditure_data
    template_name = 'datacollector_app/list.html'
    context_object_name = 'exp_data'

    def get_queryset(self):
        return(Expenditure_data.objects.filter(owener=self.request.user))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user'] = self.request.user
        data['messages'] = messages.get_messages(self.request)
        data['sum'] = amount_sum(self.request.user)
        return(data)


# add values to the database-Expenditure_data
class Add_expenditure_view(LoginRequiredMixin, CreateView):  # expenditure_data_form.html
    model = Expenditure_data
    fields = ['date', 'what_for', 'amount']

    def form_valid(self, form):
        form.instance.owener = self.request.user
        messages.success(self.request, 'Expenditure data updated successfully.')
        return(super().form_valid(form))


# clear done values from todo_list
@login_required
def clear_expenditure_table(request):
    if request.method == 'POST':
        exp = Expenditure_data.objects.filter(owener=request.user)
        exp.delete()
        messages.success(request, 'Expenditure Table cleared successfully.')
        return(redirect('dca:datacollector-home'))
    return(render(request, 'datacollector_app/list.html'))

def amount_sum(user):
    sum = 0
    exp = Expenditure_data.objects.filter(owener=user)
    for val in exp:
        sum += val.amount
    return(sum)
