from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import *

class InterviewForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(InterviewForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Enter title'

    class Meta:
        model=InterviewModel
        fields=['title','date']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

class SessionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(SessionForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Enter title'
        

    class Meta:
        model=Session
        fields=['interview','title','date','aplicant']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
