from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models import fields
from .models import Branch,Doctor,Schedule,DistrictMap
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,TimeInput
from django.contrib.admin import widgets 
from django.contrib.auth.models import User


class DistrictMapForm(forms.ModelForm):
    class Meta:
        model = DistrictMap
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'District Name','id':'name','name':'name'}),
            'latitude': TextInput(attrs={'class': 'form-control lat', 'placeholder': 'District latitude','id':'latitude','name':'latitude'}),
            'longitude': TextInput(attrs={'class': 'form-control lon', 'placeholder': 'District longitude','id':'longitude','name':'longitude'}),
        }

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch Name','id':'name','name':'name'}),
            'title': TextInput(attrs={'class': 'form-control ', 'placeholder': 'Branch Title','id':'title','name':'title'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch Phone','id':'phone','name':'phone'}),
            'location': TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch Location','id':'location','name':'location'}),
            'latitude': TextInput(attrs={'class': 'form-control lat', 'placeholder': 'Branch latitude','id':'latitude','name':'latitude'}),
            'longitude': TextInput(attrs={'class': 'form-control lon', 'placeholder': 'Branch longitude','id':'longitude','name':'longitude'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'register_number': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Register Number','id':'registernumber','name':'register_number'}),
            'name': TextInput(attrs={'class': 'form-control ', 'placeholder': 'Name','id':'name','name':'name'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'image','id':'image','name':'image'}),
            'qualification': TextInput(attrs={'class': 'form-control lat', 'placeholder': 'Designation','id':'qualification','name':'qualification'}),
            
        }


class ScheduleForm(forms.ModelForm): 
    class Meta:
        model = Schedule
        fields = '__all__'
        widgets = {
            'treatment': TextInput(attrs={'class': 'form-control', 'placeholder': 'treatment','id':'treatment','name':'treatment'}),
            'branch': Select(attrs={'class': 'form-control ','id':'branid','name':'branch'}),
            'doctor': Select(attrs={'class': 'form-control','id':'doctid','name':'doctor'}),
            'day': TextInput(attrs={'class': 'form-control', 'placeholder': 'day','id':'day','name':'day'}),
            'start_time': TimeInput(attrs={'class': 'form-control','type':'time','id':'starttime','name':'starttime'}),
            'end_time': TimeInput(attrs={'class': 'form-control','type':'time','id':'endtime','name':'endtime'}),

        }



