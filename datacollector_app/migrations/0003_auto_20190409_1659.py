# Generated by Django 2.1.7 on 2019-04-09 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacollector_app', '0002_todo_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenditure_data',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
