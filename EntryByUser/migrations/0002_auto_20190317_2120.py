# Generated by Django 2.0.5 on 2019-03-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EntryByUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataentry',
            name='date',
            field=models.DateField(),
        ),
    ]