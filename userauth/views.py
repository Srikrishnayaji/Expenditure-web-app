from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import User_register_form
from django.contrib import messages


class User_register_view(View):
    template_name = 'userauth/register.html'
    form_class = User_register_form
    model = User

    def get(self, request):
        form = self.form_class(None)
        return(render(request, self.template_name, {'form': form}))

    def post(self, request):
        form = self.form_class(request.POST)
        person = self.model()
        if form.is_valid():
            person.username = form.instance.username
            person.email = form.instance.email
            person.set_password(form.instance.password)
            person.save()
            messages.success(self.request, 'Account Created successfully. You can login now.')
            return(redirect('datastore-login'))
        else:
            return(render(request, self.template_name, {'form': self.form_class(None)}))


# delete account
def delete_account(request):
    if request.method == 'POST':
        user = User.objects.filter(username=request.user.username)
        user.delete()
        return(redirect('datastore-register'))
    else:
        return(render(request, 'userauth/delete_account.html'))
