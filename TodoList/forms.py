from django import forms
from django.db import models
from models import *


class ToDoForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'content_form', }))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'date_form', }))
    expire_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'date_form', }))

    class Meta:
        model = ToDo
        fields = "__all__"