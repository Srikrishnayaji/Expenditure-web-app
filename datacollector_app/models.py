from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# creating expenditure models
class Expenditure_data(models.Model):
    date = models.DateField()
    what_for = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=1000, decimal_places=2)
    owener = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return(f'What for?: {self.what_for}')

    def get_absolute_url(self):
        return(reverse('dca:datacollector-home'))
