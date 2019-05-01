from django import forms
from django.contrib.auth.models import User


class User_register_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_repeat = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super(User_register_form, self).clean()
        password = cleaned_data['password']
        conf_password = cleaned_data['password_repeat']
        if password == conf_password:
            return(cleaned_data)
