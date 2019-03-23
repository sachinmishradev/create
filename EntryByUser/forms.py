from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

from  .models import DataEntry

class DailyEntryForm(ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = DataEntry
        fields = '__all__'


