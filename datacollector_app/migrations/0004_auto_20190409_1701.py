# Generated by Django 2.1.7 on 2019-04-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacollector_app', '0003_auto_20190409_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenditure_data',
            name='date',
            field=models.DateField(),
        ),
    ]
