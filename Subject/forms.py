from django.forms import ModelForm
from django import forms
from .models import Subject

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'subject_msj': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; height: 30px; font-size: 12px;'}),
            'subject_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; height: 30px; font-size: 12px;'}),
            'subject_tc': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; height: 30px; font-size: 12px;'}),
        }
        labels = {
            'subject_msj': 'Mã môn học',
            'subject_name': 'Tên môn học',
            'subject_tc': 'Tín chỉ',
        }