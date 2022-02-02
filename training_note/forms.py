from django import forms

# class TaskForm(forms.Form):
#     task_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
#     task_description = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))
#     completed = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class' : 'form-control'}))
#     completed_date = forms.DateField(widget=forms.DateInput(attrs={'class' : 'form-control'}))
from django.contrib.admin.widgets import AdminDateWidget

class YourForm(forms.ModelForm):
        from_date = forms.DateField(widget=AdminDateWidget())